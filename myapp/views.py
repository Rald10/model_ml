from django.shortcuts import render
from django.http import HttpResponse
from joblib import load

# Define the path to the saved model
model = load('./savedModels/model.joblib')

def home(request):
    y_pred = None  # Initialize y_pred to avoid UnboundLocalError
    
    if request.method == 'POST':
        sepal_length = float(request.POST["sepal_length"])
        sepal_width = float(request.POST["sepal_width"])
        petal_length = float(request.POST["petal_length"])
        petal_width = float(request.POST["petal_width"])
        
        print(sepal_length)

        y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        if y_pred[0] == 0:
            y_pred = "Setosa"
        elif y_pred[0] == 1:
            y_pred = "Versicolor"
        else:
            y_pred = "Virginica"
        
        print(y_pred)
        
        return render(request, 'myapp/home.html', {'result': y_pred})
    
    # No need to print y_pred outside of the POST request
    return render(request, "myapp/home.html")
