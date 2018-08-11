
# from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from .libraries import svmModella
from .models import ctiRawTable, marketTable1, marketTable2,marketTable3,marketTable4,marketTable5,marketTable6,marketTable7,marketTable8,marketTable9,marketTable10
from django.contrib import messages
import  pandas
import datetime
# from .forms import clfFileForm
import  pandas as pd
# from csv import DictReader
import csv
from django.core.files.storage import FileSystemStorage
# from PIL import Image
from random import sample



# Create your views here.

def index(request):
    return render(request, 'mainapp/home.html')

def analysis(request):

    # accuracy = svmModella.trainn_model('Real_Deal_Export.csv')
    # accuracy = svmModella.runModel()
    # accuracy = []
    # form = clfFileForm()

    # content = {'form':form,
    #            }
    return render(request, 'mainapp/analysis.html')

# class detailView(DetailView):
#     model =  ctiRawTable
#     user = ctiRawTable.objects.get(pk=1)
#     template_name = 'mainapp/compare.html'


def compare(request,pk=None):
    if pk:
        dataDetail = ctiRawTable.objects.get(pk=pk) #the 2nd pk is from the url sent by results.html I think
    return render(request,'mainapp/compare.html',{'dataDetail':dataDetail})


def search(request):
    queryset_list = ctiRawTable.objects.all()
    marketName = ''
    if (request.GET.get("mrkNF") == '1'):
        queryset_list = marketTable1.objects.all()
        marketName = 'Agora'
    elif (request.GET.get("mrkNF") == '2'):
        queryset_list = marketTable2.objects.all()
        marketName = 'Real Deal'
    elif (request.GET.get("mrkNF") == '3'):
        queryset_list = marketTable3.objects.all()
        marketName = 'Hansa'
    elif (request.GET.get("mrkNF") == '4'):
        queryset_list = marketTable4.objects.all()
        marketName = 'Valhala'
    elif (request.GET.get("mrkNF") == '5'):
        queryset_list = marketTable5.objects.all()
        marketName = 'Tochka'
    elif (request.GET.get("mrkNF") == '6'):
        queryset_list = marketTable6.objects.all()
        marketName = 'Alpha Bay'
    elif (request.GET.get("mrkNF") == '7'):
        queryset_list = marketTable7.objects.all()
        marketName = 'EVO'
    elif (request.GET.get("mrkNF") == '8'):
        queryset_list = marketTable8.objects.all()
        marketName = 'Dream Market'
    elif (request.GET.get("mrkNF") == '9'):
        queryset_list = marketTable9.objects.all()
        marketName = 'ADM'
    elif (request.GET.get("mrkNF") == '10'):
        queryset_list = marketTable10.objects.all()
        marketName = 'Oasis'


    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(Q(description__icontains=query)).distinct()
                                             # | Q(title__icontains = query))
    resultLength = len(queryset_list)

#Pagination
    # paginator = Paginator(queryset_list, 10)  # Show 10 contacts per page
    # page = request.GET.get('page')
    # queryset = paginator.get_page(page)

    content = {'filteredList':queryset_list,
               'resultLength':resultLength,
               'marketName':marketName
              }
    return  render(request, 'mainapp/search.html',content)




def analysis_mod1(request): #code for analysis/mod1 i.e the outcome of the svm classification with first 10 or 20 rows displayed
    # file_path = request.POST.get()
    # accuracy = svmModella.runModel(file)

    # urlz= ctiRawTable.
    # Reading in the CSV file
    # if(request.method is not 'POST'):
    #     return HttpResponseRedirect(reverse("analysis"))
    verify_post = 0
    content = {'verify_post': verify_post}


    if request.method == 'POST':

        csv_file = request.FILES["csv_file"]
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'Only CSV files accepted, Please Select a CSV file')
            return HttpResponseRedirect(reverse("analysis"))

    # if file is too large, return
        if (csv_file.size > (30 *1024 *1024)):
            messages.error(request,
                           "Sorry, File Selected is too Large(%.2f MB). Ensure that the file is less than 30 MB" % (
                           csv_file.size / (1000 * 1000),))
            return HttpResponseRedirect(reverse("analysis"))
        # if csv_file.multiple_chunks():



        # file_data = csv_file.read().decode("utf-8")
        #
        # data = open(csv_file)
        # reader = csv.reader(data)
        fs = FileSystemStorage()
        file_name = fs.save(csv_file.name,csv_file)
        file_path = fs.url(file_name)

        new_file_path = file_path[1:]
        # file_path = file_path[1:]
        # df = pd.read_csv(new_file_path)

        # file_name = csv_file.name
        # lines = file_data.split("\n")
        # description = []
        # # loop over the lines and save them in db. If error , store as string and then display
        # for line in reader:
        #     # fields = line.split(",")
        #     description.append(line[0])
            # fields = line.split(",")
            # # fields[1]
        # f = lines
        # with open(file_data) as f:
        #     a1 = [row["description"] for row in DictReader(f)]
        # file_path = csv_file

        # description = []
        # for row in file_data:
        #     description.append(row[2])




        # desc = df['description']

        cyberRelevant = svmModella.runModel(new_file_path)
        market_tag = request.POST.get('market_tag')
        market_name = ''
        #initializing ample db data. To be overwritten subsequently
        sample_data_from_db = marketTable10.objects.all()

        verify_post = 1 #verify that the page was a post request



    #Save Intelligence to DB
        if(market_tag == '1'): #Agora
            marketTable1.objects.all().delete()
            for x in range(len(cyberRelevant)-1):
                saveData = marketTable1(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples


            count = marketTable1.objects.all().count()
            rand_ids = sample(range(1, count), 10)

            sample_data_from_db =marketTable1.objects.all().order_by('?')[:20]
            # sample_data_from_db = marketTable1.objects.filter().order_by('id')[:10]
            market_name = 'Agora'
        elif (market_tag == '2'): #Real Deal
            marketTable2.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable2(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable2.objects.all().order_by('?')[:20]
            market_name = 'Real Deal'
        elif (market_tag == '3'):  # Hansa
            marketTable3.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable3(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable3.objects.all().order_by('?')[:20]
            market_name = 'Hansa'
        elif (market_tag == '4'):  # Valhala
            marketTable4.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable4(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable4.objects.all().order_by('?')[:20]
            market_name = 'Valhala'
        elif (market_tag == '5'):  # Tochka
            marketTable5.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable5(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable5.objects.all().order_by('?')[:20]
            market_name = 'Tochka'
        elif (market_tag == '6'):  # Alpha Bay
            marketTable6.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable6(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable6.objects.all().order_by('?')[:20]
            market_name = 'Alpha Bay'
        elif (market_tag == '7'):  # EVO
            marketTable7.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable7(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable7.objects.all().order_by('?')[:20]
            market_name = 'EVO'
        elif (market_tag == '8'):  # Dream Market
            marketTable8.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable8(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable8.objects.all().order_by('?')[:20]
            market_name = 'Dream'
        elif (market_tag == '9'):  # ADM
            marketTable9.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable9(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            sample_data_from_db =marketTable9.objects.all().order_by('?')[:20]
            market_name = 'ADM'
        elif (market_tag == '10'):  # Oasis
            marketTable10.objects.all().delete()
            for x in range(len(cyberRelevant) - 1):
                saveData = marketTable10(description=cyberRelevant.iloc[x]['Description'])
                saveData.save()
            # querying 10 samples
            # count = marketTable1.objects.all().count()
            # rand_ids = sample(xrange(1, count), 10)

            # sample_data_from_db = marketTable1.objects.filter(id__in=rand_ids)
            # sample_data_from_db = marketTable10.objects.filter().order_by('-id')[:10]
            sample_data_from_db =marketTable10.objects.all().order_by('?')[:20]
            market_name = 'Oasis'




        content = {'cyberRelevant':cyberRelevant,
                   'type':type(cyberRelevant),
                   'sample_from_db':sample_data_from_db,
                    'verify_post':verify_post,
                   'market_name':market_name,
                   }
    # if request.method is not 'POST':
    #     return HttpResponseRedirect(reverse("analysis"))


    return render(request,'mainapp/mod1.html',content)

def analysis_mod2(request):
    #code for the outcome of the topics extraction OR just display the word Cloud and a button to view the pie chart of top 10 or 20(or as entered by user) most occuring words(using fit_transform to get the features and hence their count after removing useless words) in each Market()

   market_data_list = []
   market_data = ''
   market_name = ''
   top_n = request.POST.get('top_n')

   top_n = int(top_n)
   if (top_n > 100):
       messages.error(request,'Requested number of features must not exceed 100')
       return HttpResponseRedirect(reverse("analysis"))


   if (request.POST.get('market_name') == 'agora'):
        market_name = 'agora'
        market_data = marketTable1.objects.all()
        for listing in market_data:
            market_data_list.append(listing.description)


   elif (request.POST.get('market_name') == 'real_deal'):
        market_data = marketTable2.objects.all()
        market_name = 'real_deal'
        for listing in market_data:
            market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'hansa'):
        market_data = marketTable3.objects.all()
        market_name = 'hansa'
        for listing in market_data:
            market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'valhala'):
        market_data = marketTable4.objects.all()
        market_name = 'valhala'
        for listing in market_data:
            market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'tochka'):
            market_data = marketTable5.objects.all()
            market_name = 'tochka'
            for listing in market_data:
                market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'alpha_bay'):
        market_data = marketTable6.objects.all()
        market_name = 'alpha_bay'
        for listing in market_data:
            market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'evo'):
       market_data = marketTable7.objects.all()
       market_name = 'evo'
       for listing in market_data:
           market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'dream_market'):
           market_data = marketTable8.objects.all()
           market_name = 'dream_market'
           for listing in market_data:
               market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'adm'):
               market_data = marketTable9.objects.all()
               market_name = 'adm'
               for listing in market_data:
                   market_data_list.append(listing.description)

   elif (request.POST.get('market_name') == 'oasis'):
               market_data = marketTable10.objects.all()
               market_name = 'oasis'
               for listing in market_data:
                   market_data_list.append(listing.description)



   if (len(market_data_list) < 1):

        messages.error(request,"Market Data for " +market_name+ " market Unavailable, Please try uploading data in the Classification Section First")
        return HttpResponseRedirect(reverse("analysis"))
   #Extract the topics and save output to png file
   top_features = []
   top_features = svmModella.extractTopics(market_data_list,market_name,top_n)

#read output png file path and send to page
   word_cloud_path = svmModella.getWordCloud(market_name)

   content= {
        'word_cloud_path':word_cloud_path,
       'market_list': market_data_list,
       'market_name': market_name,
       'top_features':top_features,
       'features_length':len(top_features),
       # 'top_n':top_n,
       # 'is_market_empty':is_market_empty
    }

   return render(request,'mainapp/mod2.html',content)









