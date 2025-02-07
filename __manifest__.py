{
    'name': "school_addon",
    'version': '18.0',
    'depends': ['base'],
    'author': "My Company",
    'category': 'Uncategorized',
    'description': """
    This is the custom school model contain teacher and student information 
    """,
    # data files always loaded at installation
    # xml file and security file are imported in data
    'data': [
        'data/student.xml',
        'data/student.information.csv',
        'security/student_rules.xml',
        'security/ir.model.access.csv',
        'views/student_views.xml', 
        'views/teacher_views.xml',
    ],

    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'license':'LGPL-3',
    'installable':True,
    'application':True,
}
