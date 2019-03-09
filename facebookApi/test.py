import facebook
access_token = 'EAAgL5ZBVdwa0BALQe6aMFzgnbqkrPuLwQrOkgOSL32tCuGQK2Jm3SaPaaymdHCSfsD5tv5nZCUOoDcQYoDlLaGr2xnpx7YLWZBOLUH0UuZAQ4c2SyZBQcdiAyWrZAMSPG44E0GXdd5L3ZAn9HnaVwiilKVilvO3KsSz9hRZCCb4QiiamQLPYCtnT5W3ZBrfTU1XAZD'


graph = facebook.GraphAPI(access_token="your_token", version="2.12")
print(graph.get_permissions("me"))
# profile = graph.get_object("me")
# friends = graph.get_connections("me", "friends")

# friend_list = [friend['name'] for friend in friends['data']]

# print (friend_list)