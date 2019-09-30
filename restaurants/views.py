from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    	"my_list": [
    		{
    			"restaurant_name": "KFC",
    			"food_type": "Fried Chicken"
    		},
    		{
    			"restaurant_name": "Koji",
    			"food_type": "Japanese"
    		},
    		{
    			"restaurant_name": "PickYo",
    			"food_type": "Healthy Cafe"
    		}
    	]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	"my_object": {
    		"restaurant_name": "Tikka",
    		"food_type": "chicken"
    	}
    }
    return render(request, 'detail.html', context)
    