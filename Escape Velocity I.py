from decimal import *


def escape_velocity(planet):

    planets = {
        'Mercury': [0.0558,	0.383],
        'Jupiter': [318, 11.2],
        'Venus': [0.815, 0.95],
        'Earth': [1, 1],
        'Mars': [0.107, 0.532],
        'Saturn': [95.1, 9.41],
        'Uranus': [14.5, 4.06],
        'Neptune': [17.2, 3.88]
    }

    G_CONST = Decimal("6.67e-11")
    value = planets[planet]
    mass = Decimal(5.97600e24 * value[0])
    radius = Decimal(round(6378 * value[1], 1))

    result = Decimal((2 * G_CONST * mass) / (radius * 1000))
    result = Decimal(result.sqrt() / 1000)

    escape_velocity_kms = result.quantize(Decimal('1e-5'))
    escape_velocity_kmh = Decimal(escape_velocity_kms * 3600)
    escape_velocity_ms = escape_velocity_kms * 1000

    escape_velocity_ms = '{:.2f}'.format(escape_velocity_ms)
    escape_velocity_kms = '{:.2f}'.format(escape_velocity_kms)
    escape_velocity_kmh = '{:.2f}'.format(escape_velocity_kmh)

    title = "The escape velocity in "
    return title + "m/s is: " + escape_velocity_ms + ". " +  \
           title + "km/h is: " + escape_velocity_kmh + ". " + \
           title + "km/s is: " + escape_velocity_kms + ". "


print(escape_velocity('Jupiter'))
print(escape_velocity('Mercury'))
33