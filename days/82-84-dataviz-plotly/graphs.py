# bokeh imports
from bokeh.io import output_file, show
from bokeh.palettes import Category20b, Plasma
from bokeh.plotting import figure
from bokeh.transform import cumsum

# other needed imports
from collections import Counter
from datetime import datetime
import feedparser
from math import pi
import pandas as pd
import re

output_file("chart.html")

blog_feed = feedparser.parse('https://pybit.es/feeds/all.rss.xml')
entries = blog_feed['entries']


def let_user_choose_the_chart():
    '''Lets the user choose which chart they want to see'''
    print('A Pybites article categories')
    print('B Amount of posts per month on pybit.es')
    print('C Pybites tag popularity')
    choice = input('Which chart would you like to see?: (A/B/C) ')
    if choice.upper() == 'A':
        make_category_pie_chart()
    elif choice.upper() == 'B':
        make_posts_bar_chart()
    elif choice.upper() == 'C':
        make_tag_pie_chart()
    else:
        print('Invalid choice')
        exit()
    print('\nGood choice. Check your browser for the graph')


def get_category(link):
    '''Gets the category of the posts from the RSS feed'''
    known = dict(codechallenge='challenge',
                 twitter='news',
                 special='special',
                 guest='guest')
    default = 'article'
    category = re.sub(r'.*\.es/([a-z]+).*', r'\1', link)
    return known.get(category) or default


def format_categories(categories):
    '''Gets most common categories and puts them in a dict'''
    cnt = Counter(categories)
    categories = cnt.most_common()
    cat = {category[0]: category[1] for category in categories}
    return cat


def get_tags():
    '''Gets the 20 most common tags and puts them in a dict'''
    tags = [tag.term.lower() for entry in entries for tag in entry.tags]
    cnt = Counter(tags)
    top_tags = cnt.most_common(20)
    tags = {tag[0]: tag[1] for tag in top_tags}
    return tags


def get_year_month(date_str):
    '''Strips the day and time from the published field
        Returns the year and month'''
    #  'published': 'Sun, 07 Jan 2018 12:00:00 +0100',
    date_str = date_str.split('+')[0].strip()
    dt = datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S')
    return f'{dt.year}-{dt.month}'


def make_category_pie_chart():
    '''Makes a pie chart showing how much each category is used'''
    categories = [get_category(entry.link) for entry in entries]
    pybites_data = format_categories(categories)

    data = pd.Series(pybites_data).reset_index(name='value')\
        .rename(columns={'index': 'category'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Plasma[len(pybites_data)]
    data['legend'] = data['category'] + ': ' + data['value'].astype(str)
    p = figure(plot_height=350, title="Most common pybites categories",
               toolbar_location=None, tools="hover",
               tooltips="@category: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='legend',
            source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    show(p)
    return 'It worked'


def make_posts_bar_chart():
    '''Makes a bar chart showing the amount of posts per month'''
    pub_dates = [get_year_month(entry.published) for entry in entries]
    posts_by_month = Counter(pub_dates)
    posts = list(posts_by_month.keys())[::-1]
    count = list(posts_by_month.values())[::-1]
    posts = posts[13:]
    count = count[13:]

    p = figure(x_range=posts, plot_height=500, plot_width=1400,
               title="Posts per month",
               toolbar_location=None, tools="")

    p.vbar(x=posts, top=count, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    show(p)
    return 'It worked'


def make_tag_pie_chart():
    '''Makes a pie chart showing the popularity of each tag'''
    tags = get_tags()

    data = pd.Series(tags).reset_index(name='value')\
        .rename(columns={'index': 'tag'})
    data['angle'] = data['value'] / data['value'].sum() * 2 * pi
    data['color'] = Category20b[len(tags)]
    data['legend'] = data['tag'] + ': ' + data['value'].astype(str)
    p = figure(plot_height=600, title="Most common tags in pybites posts",
               toolbar_location=None, tools="hover",
               tooltips="@tag: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True),
            end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend='legend',
            source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    show(p)


if __name__ == '__main__':
    let_user_choose_the_chart()
