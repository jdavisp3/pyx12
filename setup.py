#from distutils import core
from distutils import core
from distutils.file_util import copy_file
from distutils.dir_util import mkpath
import cPickle
import os
import sys

import pyx12
import pyx12.map_if
import pyx12.params

map_dir = 'share/pyx12/map'
map_files = [
    'map/270.4010.X092.A1.xml',
    'map/270.4010.X092.xml',
    'map/271.4010.X092.A1.xml',
    'map/271.4010.X092.xml',
    'map/276.4010.X093.A1.xml',
    'map/276.4010.X093.xml',
    'map/277.4010.X093.A1.xml',
    'map/277.4010.X093.xml',
    'map/277U.4010.X070.xml',
    'map/277.4020.X104.xml', 
    'map/278.4010.X094.27.A1.xml',
    'map/278.4010.X094.27.xml',
    'map/278.4010.X094.A1.xml',
    'map/278.4010.X094.xml',
    'map/820.4010.X061.A1.xml',
    'map/820.4010.X061.xml',
    'map/834.4010.X095.A1.xml',
    'map/835.4010.X091.A1.xml',
    'map/835.4010.X091.xml',
    'map/837.4010.X096.A1.xml',
    'map/837.4010.X096.xml',
    'map/837.4010.X097.A1.xml',
    'map/837.4010.X097.xml',
    'map/837.4010.X098.A1.xml',
    'map/837.4010.X098.xml',
    'map/841.4010.XXXC.xml',
    'map/997.4010.xml',
    'map/x12.control.00401.xml' 
]

mkpath('build/bin')
SCRIPTS = ('x12_build_pkl', 'x12html', 'x12info', 'x12valid', 
    'x12norm', 'x12sql', 'x12xml', 'xmlx12')
for filename in SCRIPTS:
    copy_file(os.path.join('bin', filename+'.py'), 
        os.path.join('build/bin', filename))
TEST_FILES = ['test/%s' % (file1) for file1 in 
    filter(lambda x: x[:4] == 'test' and os.path.splitext(x)[1] == '.py',
    os.listdir('test'))]
TEST_DATA = ['test/files/%s' % (file1) for file1 in 
    filter(lambda x: os.path.splitext(x)[1] 
        in ('.base', '.txt', '.idtag', '.idtagqual', '.simple'),
    os.listdir('test/files'))]
    
kw = {  
    'name': "pyx12",
    'version': pyx12.__version__,
    'description': pyx12.__doc__,
    #'description': "A X12 validator and converter",
    'author': "John Holland",
    'author_email': "jholland@kazoocmh.org",
    'url': "http://www.sourceforge.net/pyx12/",
    'packages': ['pyx12'],
    'scripts': ['build/bin/%s' % (script) for script in SCRIPTS],
    'data_files': [
        (map_dir, map_files),
        (map_dir, ['map/README', 'map/codes.xml', 'map/codes.xsd',
        'map/comp_test.xml', 'map/map.xsd', 'map/maps.xml', 
        'map/x12simple.dtd']),
        ('share/doc/pyx12', ['README.txt', 'LICENSE.txt',
        'CHANGELOG.txt', 'INSTALL.txt']),
        ('share/examples/pyx12/test', TEST_FILES),
        ('share/examples/pyx12/test/files', TEST_DATA),
        ('share/examples/pyx12', ['bin/pyx12.conf.xml.sample']),
        ('etc', ['bin/pyx12.conf.xml.sample']),
        ('share/doc/pyx12/view', ['view/Makefile', 'view/codes.xsl', \
            'view/loop.css', 'view/loop.xsl', 'view/map_seg.xsl', \
            'view/map_sum.xsl', 'view/seg.css', 'view/sum.css',
            'view/none.css', 'view/plain.css'])    
    ],
      #package_dir = {'': ''},
}

if (hasattr(core, 'setup_keywords') and
    'classifiers' in core.setup_keywords):
    kw['classifiers'] = \
        ['Topic :: Communications, Office/Business',
         'Environment :: Console (Text Based)',
         'Intended Audience :: Developers, Other Audience',
         ' License :: OSI Approved :: BSD License'],

param = pyx12.params.params()
for file in map_files:
    param.set('map_path', 'map')
    map_file = os.path.basename(file)

core.setup(**kw)
