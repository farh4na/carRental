from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from user.models import Car, Profile
from .forms import SearchForm
from .forms import ProfileForm
from .fuzzy_logic import get_recommendation # Import the function for recommendation

# Create your views here.
def home(request):
    cars = Car.objects.all()  # Fetch all cars; you can 
    return render(request, 'home.html', {'cars': cars})  # This is the HTML file to display

def register(request):
    if request.user.is_authenticated:
        return redirect("home") # Redirect if user is already logged in
    
    if request.method == "POST":
        # Extract form data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')

        # Validate form data
        if not all([username, email, password, confirm_password, phone_number, address]):
            messages.error(request, "All fields are required!")
            return redirect('register')

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')
        
        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            Profile.objects.create(user=user, phone_number=phone_number, address=address)
            user.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')  # Redirect to login page
        except Exception as e:
            messages.error(request, f"An error occurred: {e}")
            return redirect('register')

    return render(request, 'register.html')

def login_view(request):
    if request.user.is_authenticated:
        messages.info(request, "You are already logged in!")
        return redirect("home")

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate inputs
        if not username or not password:
            messages.error(request, "Both username and password are required!")
            return redirect('login')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  # Use the built-in login function
            messages.success(request, "Welcome back!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')

    return render(request, 'login.html')

@login_required
def editprofile(request):
    user = request.user  # Get the logged-in user

    if request.method == "POST":
        # Get the new email from the form
        new_email = request.POST.get('email')
        new_username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        new_phone_number = request.POST.get('phone_number')
        new_address = request.POST.get('address')

        # Handle password change
        if password and password == confirm_password:
            user.set_password(password)  # Set the new password
        else:
            if password != confirm_password:
                messages.error(request, "Passwords do not match!")
                return redirect('editprofile')

        # Update user fields (e.g., username and email)
        user.username = new_username
        user.email = new_email
        Profile.phone_number = new_phone_number
        Profile.address = new_address

        try:
            user.save()  # Save the updated user fields
            Profile.save()  # Save the profile changes
            messages.success(request, "Profile updated successfully!")
            return redirect('editprofile')
        except Exception as e:
            messages.error(request, f"Error updating user information: {e}")
            return redirect('editprofile')


    # If the request is GET, pre-populate the form with existing user data
    return render(request, 'editprofile.html', {'user': user,  'profile': Profile})


def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def recommend_car_view(request):
    
    if request.method == 'POST':
        # Extract form data
        location = request.POST.get('location')
        pickup_date = request.POST.get('pickup_date')
        pickup_time = request.POST.get('pickup_time')
        return_date = request.POST.get('return_date')
        return_time = request.POST.get('return_time')
        car_type = request.POST.get('car_type')
        transmission = request.POST.get('transmission')
        brand = request.POST.get('brand')
        seats = int(request.POST.get('seats', 0))
        price_range = request.POST.get('price_range')
        
        # Convert form data to numeric values for fuzzy logic
        car_type_value = {'sedan': 0, 'suv': 1, 'hatchback': 2}.get(car_type, 0)
        transmission_value = {'auto': 0, 'manual': 1}.get(transmission, 0)
        brand_value = {'proton': 0, 'perodua': 1, 'honda': 2, 'toyota': 3}.get(brand, 0)
        seats_value = {5: 0, 7: 1}.get(seats, 0)
        price_range_value = {'0-200': 0, '>200': 1}.get(price_range, 0)

        print(f"Car Type: {car_type_value}")
        print(f"Transmission: {transmission_value}")
        print(f"Brand: {brand_value}")
        print(f"Seats: {seats_value}")
        print(f"Price Range: {price_range_value}")

        # Validate form data (basic checks)
        if not car_type or not transmission or not brand or not price_range or seats == 0:
            # Optionally, you can display a message to inform the user that some fields are missing
            context = {'error_message': 'Please fill out all fields properly.'}
            return render(request, 'home.html', context)
        
         # Run the fuzzy logic function to get the recommendation
        recommended_car = get_recommendation(car_type_value, transmission_value, brand_value, seats_value, price_range_value)

         # Pass the recommendation to the template
        context = { 
            'recommended_car': recommended_car,
            'car_type': car_type,
            'transmission': transmission,
            'brand': brand,
            'seats': seats,
            'price_range': price_range,
            'location': location,
            'pickup_date': pickup_date,
            'pickup_time': pickup_time,
            'return_date': return_date,
            'return_time': return_time
        }
        return render(request, 'recommend_car.html', context)

    # Render the form for GET request
    return render(request, 'home.html')
            
    


















































def recommend_car(request):
    if request.method == "POST":
        # Get input from the form
        location = request.POST.get("location")
        pickup_date = request.POST.get("pickup_date")
        pickup_time = request.POST.get("pickup_time")
        return_date = request.POST.get("return_date")
        return_time = request.POST.get("return_time")
        car_type = request.POST.get("car_type")
        transmission = request.POST.get("transmission")
        brand = request.POST.get("brand")
        seats = request.POST.get("seats")
        price_range = request.POST.get("price_range")

         # Convert `seats` to integer safely
        seats = int(seats) if seats and seats.isdigit() else None


         # Create filter dictionary dynamically
        filters = {}
        if car_type: filters["car_type__iexact"] = car_type
        if transmission: filters["transmission__iexact"] = transmission
        if brand: filters["brand__iexact"] = brand
        if seats: filters["seats"] = seats
        if price_range: filters["price_range__iexact"] = price_range

        # Get first matching car
        recommended_car = Car.objects.filter(**filters).first()

        context = {
            "recommended_car": recommended_car,
            "location": location,
            "pickup_date": pickup_date,
            "pickup_time": pickup_time,
            "return_date": return_date,
            "return_time": return_time,
            "car_type": car_type,
            "transmission": transmission,
            "brand": brand,
            "seats": seats,
            "price_range": price_range,
        }

        return render(request, "recommend_car.html", context)

    return render(request, "home.html")







