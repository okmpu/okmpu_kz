# from django.shortcuts import get_object_or_404, render
# from main.public.models import News, Announcement, Event
#
#
# # News pages
# def news_view(request, pk=None):
#     if pk:
#         item = get_object_or_404(News, pk=pk)
#         similar_items = News.objects.exclude(pk=item.pk)[:5]
#         context = {
#             'code': 'news',
#             'item': item,
#             'similar_items': similar_items
#         }
#         return render(request, 'src/publics/public_detail.html', context)
#     else:
#         items = News.objects.all()
#         context = {
#             'code': 'news',
#             'items': items
#         }
#         return render(request, 'src/publics/index.html', context)
#
#
# # Announcement pages
# def announcement_view(request, pk=None):
#     if pk:
#         item = get_object_or_404(Announcement, pk=pk)
#         similar_items = Announcement.objects.exclude(pk=item.pk)[:5]
#         context = {
#             'code': 'announcement',
#             'item': item,
#             'similar_items': similar_items
#         }
#         return render(request, 'src/publics/public_detail.html', context)
#     else:
#         items = Announcement.objects.all()
#         context = {
#             'code': 'announcement',
#             'items': items
#         }
#         return render(request, 'src/publics/index.html', context)
#
#
# # Event pages
# def event_view(request, pk=None):
#     if pk:
#         item = get_object_or_404(Event, pk=pk)
#         similar_items = Event.objects.exclude(pk=item.pk)[:5]
#         context = {
#             'code': 'event',
#             'item': item,
#             'similar_items': similar_items
#         }
#         return render(request, 'src/publics/public_detail.html', context)
#     else:
#         items = Event.objects.all()
#         context = {
#             'code': 'event',
#             'items': items
#         }
#         return render(request, 'src/publics/index.html', context)
