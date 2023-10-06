<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Weather App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
        }

        h1 {
            text-align: center;
            margin-top: 20px;
            color: #333;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #fff;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        form {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }

        input[type="text"] {
            padding: 10px;
            width: 60%;
            border: 1px solid #ccc;
            border-radius: 5px;
            margin-right: 10px;
        }

        input[type="submit"] {
            background-color: #333;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .city-box {
            background-color: #f8f8f8;
            border: 1px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            margin: 10px 0;
        }

        .city-name {
            font-size: 20px;
            font-weight: bold;
            color: #333;
        }

        .city-temp {
            font-size: 24px;
            color: #555;
        }

        .weather-icon {
            width: 50px;
            height: 50px;
        }

        .city-description {
            color: #777;
        }

        button {
            background-color: #ff3c3c;
            color: #fff;
            padding: 5px 10px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button a {
            color: #fff;
            text-decoration: none;
        }

        hr {
            margin: 10px 0;
            border: 0.5px solid #ccc;
        }
    </style>
</head>
<body>
    <h1>Weather App</h1>
    
    {% if messages %}
        {% for message in messages %}
            {{ message }}
        {% endfor %}
    {% endif %}
    <br>
    
    <div class="container">
        <form action="" method="get">
            <input type="text" name="name" placeholder="Enter a city">
            <input type="submit" value="Add">
        </form>
    
        {% for city in city_data %}
            <div class="city-box">
                <div class="city-name">{{ city.city }}</div>
                <div class="city-temp">{{ city.temp }} <span>&#8451;</span></div>
                <img class="weather-icon" src="http://openweathermap.org/img/wn/{{ city.icon }}.png" alt="Icon">
                <div class="city-description">{{ city.desc }}</div>
                <button>
                    <a href="{% url 'delete' city.city.id %}">Delete</a>
                </button>
            </div>
            <hr>
        {% endfor %}
    </div>
</body>
</html>
