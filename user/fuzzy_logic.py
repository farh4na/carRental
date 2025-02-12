import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from .models import Car

def recommend_car(price_range, car_type, transmission, brand, seats):
        # Define input variables
        car_type_ctrl = ctrl.Antecedent(np.arange(0, 3.1, 0.1), 'car_type')
        transmission_ctrl = ctrl.Antecedent(np.arange(0, 2.1, 0.1), 'transmission')
        brand_ctrl = ctrl.Antecedent(np.arange(0, 4.1, 0.1), 'brand')
        seats_ctrl = ctrl.Antecedent(np.arange(0, 7.1, 0.1), 'seats')
        price_range_ctrl = ctrl.Antecedent(np.arange(0, 1001, 1), 'price_range')

        # Define output variable (recommendation score)
        recommendation = ctrl.Consequent(np.arange(0, 11, 1), 'recommendation')

        # Define membership functions for inputs
        car_type_ctrl['sedan'] = fuzz.trimf(car_type_ctrl.universe, [0, 0.5, 1])
        car_type_ctrl['suv'] = fuzz.trimf(car_type_ctrl.universe, [1, 1.5, 2])
        car_type_ctrl['hatchback'] = fuzz.trimf(car_type_ctrl.universe, [2, 2.5, 3])

        transmission_ctrl['auto'] = fuzz.trimf(transmission_ctrl.universe, [0, 0.5, 1])
        transmission_ctrl['manual'] = fuzz.trimf(transmission_ctrl.universe, [1, 1.5, 2])

        brand_ctrl['proton'] = fuzz.trimf(brand_ctrl.universe, [0, 0.5, 1])
        brand_ctrl['perodua'] = fuzz.trimf(brand_ctrl.universe, [1, 1.5, 2])
        brand_ctrl['honda'] = fuzz.trimf(brand_ctrl.universe, [2, 2.5, 3])
        brand_ctrl['toyota'] = fuzz.trimf(brand_ctrl.universe, [3, 3.5, 4])

        seats_ctrl['5'] = fuzz.trimf(seats_ctrl.universe, [0, 2.5, 5])
        seats_ctrl['7'] = fuzz.trimf(seats_ctrl.universe, [5, 6, 7])

        price_range_ctrl['0-200'] = fuzz.trapf(price_range_ctrl.universe, [0, 0, 150, 200])
        price_range_ctrl['>200'] = fuzz.trap(price_range_ctrl.universe, [200, 500, 1000, 1000])

        # Define membership functions for output
        recommendation['Proton Saga'] = fuzz.trimf(recommendation.universe, [0, 0, 1])
        recommendation['Perodua Bezza'] = fuzz.trimf(recommendation.universe, [1, 1, 2])
        recommendation['Toyota Fortuner'] = fuzz.trimf(recommendation.universe, [2, 2, 3])
        recommendation['Honda CR-V'] = fuzz.trimf(recommendation.universe, [3, 3, 4])
        recommendation['Perodua Myvi'] = fuzz.trimf(recommendation.universe, [4, 4, 5])
        recommendation['Proton Iriz'] = fuzz.trimf(recommendation.universe, [5, 5, 6])
        recommendation['Honda City'] = fuzz.trimf(recommendation.universe, [6, 6, 7])
        recommendation['Toyota Vios'] = fuzz.trimf(recommendation.universe, [7, 7, 8])
        recommendation['Proton X70'] = fuzz.trimf(recommendation.universe, [8, 8, 9])
        recommendation['Perodua Aruz'] = fuzz.trimf(recommendation.universe, [9, 9, 10])
        recommendation['Proton Iriz'] = fuzz.trimf(recommendation.universe, [10, 10, 11])
        recommendation['Toyota Innova'] = fuzz.trimf(recommendation.universe, [11, 11, 12])
        recommendation['Proton Persona'] = fuzz.trimf(recommendation.universe, [12, 12, 13])
        recommendation['Toyota Highlander'] = fuzz.trimf(recommendation.universe, [13, 13, 14])
        recommendation['Perodua Axia'] = fuzz.trimf(recommendation.universe, [14, 14, 15])
        recommendation['Toyota Harrier'] = fuzz.trimf(recommendation.universe, [15, 15, 16])
        recommendation['Proton X50'] = fuzz.trimf(recommendation.universe, [16, 16, 17])
        recommendation['Perodua Ativa'] = fuzz.trimf(recommendation.universe, [17, 17, 18])
        recommendation['Honda Jazz'] = fuzz.trimf(recommendation.universe, [18, 18, 19])
        recommendation['Toyota Yaris'] = fuzz.trimf(recommendation.universe, [19, 19, 20])
        recommendation['Proton Inspira'] = fuzz.trimf(recommendation.universe, [20, 20, 21])
        recommendation['Perodua Bezza'] = fuzz.trimf(recommendation.universe, [21, 21, 22])
        recommendation['Honda HR-V'] = fuzz.trimf(recommendation.universe, [22, 22, 23])
        recommendation['Toyota Corolla Cross'] = fuzz.trimf(recommendation.universe, [23, 23, 24])
        recommendation['Proton Satria'] = fuzz.trimf(recommendation.universe, [24, 24, 25])
        recommendation['Perodua Myvi'] = fuzz.trimf(recommendation.universe, [25, 25, 26])
        recommendation['Proton X90'] = fuzz.trimf(recommendation.universe, [26, 26, 27])
        recommendation['Honda Pilot'] = fuzz.trimf(recommendation.universe, [27, 27, 28])
        recommendation['Perodua Alza'] = fuzz.trimf(recommendation.universe, [28, 28, 29])
        recommendation['Honda Civic Hatchback'] = fuzz.trimf(recommendation.universe, [29, 29, 30])
        recommendation['Toyota RAV4'] = fuzz.trimf(recommendation.universe, [30, 30, 31])
        recommendation['Perodua Axia'] = fuzz.trimf(recommendation.universe, [31, 31, 32])
        recommendation['Honda Civic'] = fuzz.trimf(recommendation.universe, [32, 32, 33])
        recommendation['Toyota Camry'] = fuzz.trimf(recommendation.universe, [33, 33, 34])
        recommendation['Proton Perdana'] = fuzz.trimf(recommendation.universe, [34, 34, 35])
        recommendation['Toyota Corolla'] = fuzz.trimf(recommendation.universe, [35, 35, 36])
        recommendation['Proton Preve'] = fuzz.trimf(recommendation.universe, [36, 36, 37])
        recommendation['Toyota Prius'] = fuzz.trimf(recommendation.universe, [37, 37, 38])
        recommendation['Proton Wira'] = fuzz.trimf(recommendation.universe, [38, 38, 39])
        recommendation['Perodua Kelisa'] = fuzz.trimf(recommendation.universe, [39, 39, 40])
        recommendation['Proton S70'] = fuzz.trimf(recommendation.universe, [40, 40, 41])
        recommendation['Honda Accord'] = fuzz.trimf(recommendation.universe, [41, 41, 42])
        recommendation['Toyota Vios'] = fuzz.trimf(recommendation.universe, [42, 42, 43])
        recommendation['Perodua Viva'] = fuzz.trimf(recommendation.universe, [43, 43, 44])
        recommendation['Proton Waja'] = fuzz.trimf(recommendation.universe, [44, 44, 45])
        recommendation['Honda Civic 2022'] = fuzz.trimf(recommendation.universe, [45, 45, 46])

        # Define rules
        rules = [
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Saga']), #1
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Bezza']), #2
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['7'], recommendation['Toyota Fortuner']), #3
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['7'], recommendation['Honda CR-V']), #4
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Myvi']), #5
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Iriz']), #6
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda City']), #7
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['manual'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Vios']), #8
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['7'], recommendation['Proton X70']), #9
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['7'], recommendation['Perodua Aruz']), #10
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Iriz']), #11
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['7'], recommendation['Toyota Innova']), #12
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Persona']), #13
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['7'], recommendation['Toyota Highlander']), #14
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Axia']), #15
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['7'], recommendation['Toyota Harrier']), #16
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton X50']), #17
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Ativa']), #18
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Jazz']), #19
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Yaris']), #20
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Inspira']), #21
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['manual'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Bezza']), #22
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda HR-V']), #23
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Corolla Cross']), #24
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Satria']), #25
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Myvi']), #26
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['7'], recommendation['Proton X90']), #27
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Pilot']), #28
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['7'], recommendation['Perodua Alza']), #29
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Civic Hatchback']), #30
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['suv'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota RAV4']), #31
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Axia']), #32
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Civic']), #33
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Camry']), #34
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Perdana']), #35
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Corolla']), #36
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Preve']), #37
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Prius']), #38
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['manual'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Wira']), #39
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Kelisa']), #40
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton S70']), #41
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Accord']), #42
            ctrl.Rule(price_range_ctrl['>200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['toyota'] & seats_ctrl['5'], recommendation['Toyota Vios']), #43
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['auto'] & brand_ctrl['perodua'] & seats_ctrl['5'], recommendation['Perodua Viva']), #44
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['sedan'] & transmission_ctrl['auto'] & brand_ctrl['proton'] & seats_ctrl['5'], recommendation['Proton Waja']), #45
            ctrl.Rule(price_range_ctrl['0-200'] & car_type_ctrl['hatchback'] & transmission_ctrl['manual'] & brand_ctrl['honda'] & seats_ctrl['5'], recommendation['Honda Civic']), #46
        ]

        # Create control system
        recommendation_system = ctrl.ControlSystem(rules)
        recommendation_simulation = ctrl.ControlSystemSimulation(recommendation_system)

        # Set inputs based on user selections (converting user inputs to fuzzy values)
        recommendation_simulation.input['car_type'] = car_type
        recommendation_simulation.input['transmission'] = transmission
        recommendation_simulation.input['brand'] = brand
        recommendation_simulation.input['seats'] = seats
        recommendation_simulation.input['price_range'] = price_range

        
        # print(f"Recommendation Simulation Initialized: {recommendation_simulation}")
        recommendation_simulation.compute()
        print("Recommendation Output:", recommendation_simulation.output)
        # print("Before fuzzy computation")
        
        # try:            
        #     recommendation_simulation.compute() # Compute the output (recommendation score)
        #     print(f"Recommendation Score: {recommendation_simulation.output['recommendation']}")
        # except Exception as e:
        #     print(f"Error during fuzzy computation: {e}")

        # # Log the recommendation score
        # print(f"Recommendation Score: {recommendation_simulation.output['recommendation']}")

        # # Log the recommendation output
        # print(f"Recommendation Output: {recommendation_simulation.output}")
        
        # Ensure the output exists before accessing it
        if 'recommendation' in recommendation_simulation.output:
            recommendation_score = recommendation_simulation.output['recommendation']
        else:
            recommendation_score = None

        # Query the database based on the highest recommendation score
        recommended_car = None
        if recommendation_score is not None:
            if recommendation_score < 1:
                recommended_car = Car.objects.filter(name="Proton Saga").first()
            elif recommendation_score < 2:
                recommended_car = Car.objects.filter(name="Perodua Bezza").first()
            elif recommendation_score >= 2:
                recommended_car = Car.objects.filter(name="Toyota Fortuner").first()

        return recommended_car

# The main function that handles the recommendation (possibly used in views.py)
def get_recommendation(price_range, car_type, transmission, brand, seats):
    # Convert form inputs to appropriate fuzzy values (mapping strings to numeric)
    car_type_value = {'sedan': 0, 'suv': 1, 'hatchback': 2}.get(car_type, 0)
    transmission_value = {'auto': 0, 'manual': 1}.get(transmission, 0)
    brand_value = {'proton': 0, 'perodua': 1, 'honda': 2, 'toyota': 3}.get(brand, 0)
    seats_value = {5: 0, 7: 1}.get(seats, 0)
    price_range_value = {'0-200': 0, '>200': 1}.get(price_range, 0)

    
    # Use fuzzy logic to recommend the car
    recommended_car = recommend_car(price_range_value, car_type_value, transmission_value, brand_value, seats_value)
    return recommended_car

    