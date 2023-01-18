{
    'name': 'Movie Booking',
    'version':'1.0',
    'category':'E-commerce',
    'author':'Archana',
    'summary':'book your movie ticket online',
    'description':'online movie booking management',
    'installable':True,
    'application':True,
    'data':[
        'security/ir.model.access.csv',
        'views/movie_actions.xml',
        'views/movie_views.xml',
        'views/movie_menus.xml',
        'views/movie_show_view.xml',
        'views/movie_seating_template_view.xml',
        'views/movie_type_view.xml',
        'views/movie_language_view.xml',
    ]
}