from django.shortcuts import render, HttpResponse
from history.models import SearchHistory


def home(request):
    # if request.method == 'POST':
    #     datef = request.POST.get('datef')
    #     datet = request.POST.get('datet')
    #     checkbox = request.POST.get('checkbox')
    #     filter_data = SearchHistory.objects.raw(
    #         'select * from history_searchhistory where search_time between "'+datef+'" and "'+datet+'"')

    #     distinct_user = SearchHistory.objects.values('user').distinct()
    #     distinct_keywords = SearchHistory.objects.values('keywords').distinct()
    #     index = {'data': filter_data,
    #              'dis_user': distinct_user,
    #              'dis_keyword': distinct_keywords
    #              }
    #     return render(request, 'index.html', index)
    # else:
    display_data = SearchHistory.objects.all()
    distinct_user = SearchHistory.objects.values('user').distinct()
    # print(SearchHistory.objects.values('keywords'))
    # count keywords
    keylist = []
    countKeylist = []
    for i in SearchHistory.objects.values('keywords'):
        keylist.append(i['keywords'])

    for i in SearchHistory.objects.values('keywords').distinct():
        # countKeylist[i['keywords']] = keylist.count(i['keywords'])
        countKeylist.append(
            {'keywords': i['keywords'], 'count': keylist.count(i['keywords'])})

    # SearchHistory.objects.values('keywords').distinct()
    distinct_keywords = countKeylist

    index = {'data': display_data,
             'dis_user': distinct_user,
             'dis_keyword': distinct_keywords,
             }

    return render(request, 'index.html', index)

# def home(request):
#     if request.method == 'POST':
#         checkbox = request.POST.get('checkbox')
#         filter_data = SearchHistory.objects.raw(
#             'select * from history_searchhistory where keywords="'+checkbox+'"')
#         distinct_user = SearchHistory.objects.values('user').distinct()
#         distinct_keywords = SearchHistory.objects.values('keywords').distinct()
#         index = {'data': filter_data,
#                  'dis_user': distinct_user,
#                  'dis_keyword': distinct_keywords
#                  }
#         return render(request, 'index.html', index)
#     else:
#         display_data = SearchHistory.objects.all()
#         distinct_user = SearchHistory.objects.values('user').distinct()
#         distinct_keywords = SearchHistory.objects.values('keywords').distinct()
#         index = {'data': display_data,
#                  'dis_user': distinct_user,
#                  'dis_keyword': distinct_keywords
#                  }

#         return render(request, 'index.html', index)
