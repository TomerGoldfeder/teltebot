from distutils.core import setup
setup(
  name = 'teltebot',
  packages = ['teltebot'],
  version = '0.1',
  license='MIT',
  description = 'Tensorflow Telegram Bot notifier',
  author = 'Tomer Goldfeder',
  author_email = 'goldfedertomer@gmail.com',
  url = 'https://github.com/TomerGoldfeder',
  download_url = 'https://github.com/TomerGoldfeder/teltebot/archive/0.1.tar.gz',    # I explain this later on
  keywords = ['Tensorflow', 'Telegram', 'Bot'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'matplotlib'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)