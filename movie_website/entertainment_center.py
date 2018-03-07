import media
import fresh_tomatoes

# Defining instances of Movie class with my favorite ones
spirited_away = media.Movie('Spirited Away', 'A girl wanders into a world '
                            'ruled by gods, witches and spirits',
                            'https://images-na.ssl-images-amazon.com/images'
                            '/I/51mbLUVb29L.jpg',
                            'https://youtu.be/ByXuk9QqQkk')

clockwork_orange = media.Movie('Clockwork Orange', 'A sadistic gang leader '
                               'is imprisoned and volunteers for experiment',
                               'https://images-na.ssl-images-amazon.com/images'
                               '/I/41l-eksvVrL.jpg',
                               'https://youtu.be/xHFPi_3kc1U')

eternal_sunshine = media.Movie('Eternal Sunshine of The Spotless Mind',
                               'Man erases unwanted memories',
                               'https://images-na.ssl-images-amazon.com/'
                               'images/I/51%2Bwf-vBCUL._SY450_.jpg',
                               'https://youtu.be/GBEke6JixyE')

pulp_fiction = media.Movie('Pulp Fiction',
                           'Four tales of violence and redemption',
                           'https://upload.wikimedia.org/wikipedia/en/3/3b/'
                           'Pulp_Fiction_%281994%29_poster.jpg',
                           'https://youtu.be/tGpTpVyI_OQ')

city_of_god = media.Movie('City of God',
                          'Two boys growing up in a violent neighborhood of'
                          'Rio de Janeiro take different paths',
                          'https://upload.wikimedia.org/wikipedia/en/1/10'
                          '/CidadedeDeus.jpg', 'https://youtu.be/ldVlSKByUtg')

fight_club = media.Movie('Fight Club',
                         'An insomniac office worker crosses paths with a '
                         'devil-may-care soapmaker',
                         'https://upload.wikimedia.org/wikipedia/en/f/fc/'
                         'Fight_Club_poster.jpg',
                         'https://youtu.be/SUXWAEX2jlg')

# This list groups all my favorite Movie objects
movies = [pulp_fiction, spirited_away, eternal_sunshine, fight_club,
          city_of_god, clockwork_orange]

# Using open_movies_page() method to create the trailers page
fresh_tomatoes.open_movies_page(movies)
