#需求3:完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序;
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]

data_list.sort()#默认排序
print(data_list)
data_list.sort(key = lambda list: len(list))#按照元素字符个数排序
print(data_list)
#反转排序
data_list.sort(key = lambda list: len(list), reverse=True)
print(data_list)