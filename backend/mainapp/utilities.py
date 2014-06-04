from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
def paginate(page, items_list):
  paginator = Paginator(items_list, 25) # Show 25 contacts per page
  try:
    items_list = paginator.page(page)
  except PageNotAnInteger:
    # If page is not an integer, deliver first page.
    items_list = paginator.page(1)
  except EmptyPage:
    # If page is out of range (e.g. 9999), deliver last page of results.
    items_list = paginator.page(paginator.num_pages)
  return items_list