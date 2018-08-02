from setuptools import setup


with open('README.md') as stream:
    readme_md = stream.read()


setup(name="grfc",
      author="Gus Castles",
      author_email="guscastles@gmail.com",
      url="https://github.com/guscastles/grfc/",
      description="GRFC Statistics App",
      long_description=readme_md,
      packages=["grfc", "grfc.game", "app"],
      version="0.1.0",
)
