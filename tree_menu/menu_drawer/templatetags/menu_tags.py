from django import template

from menu_drawer.models import Folder

register = template.Library()

@register.inclusion_tag('menu_drawer/menu_tree.html', takes_context=True)
def draw_menu(context, menu_name):
    '''отрисовку дерева можно производить и по слагу, в таком случае все id,
    надо заменить на slug-поле, предварительно добавив таковой в модель'''
    def get_path(query, current_folder_id):
        '''Получаем список элементов, потомков которых будем
        забирать для построения дерева(элементы, которые входят 
        в путь до нужной папки)'''
        result = [current_folder_id, ]
        if not current_folder_id: 
            return result
        for folder in query:
            if folder['id'] == current_folder_id:
                path = get_path(query, folder['parent_id'])
                print('!!!RETURNING: ', path)
                return result + path
        return [None, ]
                
    def list_to_dict(source_list, key_field):
        '''раскладываем элементы списка в словарь списков по значению
        ключа key_field, для ускорения навигации по элементам'''
        result = {}
        for folder in source_list:
            item_key_value = folder[key_field]
            if item_key_value in result:
                result[item_key_value].append(folder)
            else:
                result[item_key_value] = [folder, ]
        return result
    
    def get_childs(parent_dict, path, space, parent=None):
        '''Получаем детей текущего элемента parent из словаря parent_dict, 
        в котором ключ - id родителя, значение - список детей'''
        res = []
        if parent:
            parent_id = parent['id']
        else:
            parent_id = None
        if parent_id in parent_dict:
            for i in parent_dict[parent_id]:
                i['space'] = space
                res.append(i)
                if i['id'] in path:
                    '''space отображает уровень вложенности и от него зависит 
                    отступ при рендеринге меню'''
                    res += get_childs(parent_dict, path, space + 20, i)
        return res

    def get_link(params, name, value):
        '''формируем ссылку для каждой папки, меняя значение, 
        соответствующее текущему меню на id папки и оставляя 
        остальные элементы без изменений'''
        chain = [f'{name}={value}']
        for i in params:
            if i != name:
                chain.append(f'{i}={params[i]}')
        return '&'.join(chain)

    folders_list = list(Folder.objects.filter(menu=menu_name).values())
    url_params = context.request.GET
    root = {
        'name': menu_name if folders_list else '',
        'url': '?' + get_link(url_params, menu_name, None)}
    try: current_id = int(url_params.get(menu_name))
    except: current_id = None

    parents_dict = list_to_dict(folders_list, 'parent_id')
    folder_path =  get_path(folders_list, current_id)
    tree = get_childs(parents_dict, folder_path, 20)

    for folder in tree:
        folder['url'] = '?' + get_link(url_params, menu_name, folder['id'])

    return {'tree': tree, 'root': root}
