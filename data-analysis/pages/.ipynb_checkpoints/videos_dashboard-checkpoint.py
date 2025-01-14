# --------------------------Import packeges----------------------
from dash import html, callback, Input, Output, register_page, dcc
import dash
import plotly.express as px
import plotly.io as pio
from datetime import datetime
import pandas as pd

pio.templates.default = "ggplot2"
# ---------------------------------------------------------------


# -------------Reading data and setting constants----------------
videos_like_per_country              = pio.read_json("data-analysis/plots/json/videos_like_per_country.json")
video_stats_growth_per_time          = pio.read_json("data-analysis/plots/json/video_stats_growth_per_time.json")
social_accounts_affect_on_vid_stats  = pio.read_json("data-analysis/plots/json/social_accounts_affect_on_vid_stats.json")
duration_vs_views                    = pio.read_json("data-analysis/plots/json/desc_len_vs_views_scatter_plot.json")
likes_vs_views                       = pio.read_json("data-analysis/plots/json/likes_vs_views_bubble_chart.json")
video_stats_per_tag                  = pio.read_json("data-analysis/plots/json/video_stats_per_tag.json")

    
THEME_COLORS = ["#2e2e2e", "#fc0303"]
EXERNAL_STYLESHEETS = ['assets/style.css']
TODAY = datetime.now().strftime("%Y-%m-%d")

DISTANCE: int = 5
SPACE_DISTANCE = 0
N_WIDTH: int = 600 # normal width
L_WIDTH: int = (N_WIDTH * 2) + DISTANCE # large width

N_HEIGHT: int = 500
L_HEIGHT: int = (N_HEIGHT * 2) + DISTANCE
# ---------------------------------------------------------------


# ------------------Creating the dashboard-----------------------
register_page(__name__)
# app = dash.Dash(__name__)

layout = html.Div(children= [
    
    html.Center(children= html.H2(children= [html.Span(
        "Gaming", style= {"color": THEME_COLORS[1]}), " Videos Dashboard"])),
    
    
    dcc.Graph(
        id='videos_like_per_country',
        figure= videos_like_per_country.update_layout(width= N_WIDTH, height= N_HEIGHT),
        
        style= {'position': 'relative', 'padding':'5px',
                'display': 'inline-block', "right" : f"{DISTANCE}px", "bottom": f"{N_HEIGHT + 2}px",
                'border-radius': '20px', 'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)'},
        
        config= {'displaylogo': False}),
    
    
    dcc.Graph(
        id= 'social_accounts_affect_on_vid_stats',
        figure= social_accounts_affect_on_vid_stats.update_layout(width= N_WIDTH,
                                                                  height= L_HEIGHT + (DISTANCE * 2)),
        
        style= {'position': 'relative', 'padding':'5px',
                'display': 'inline-block', 'left': f'{DISTANCE * 2}px', 'top': f'{DISTANCE * 2}px',
                'border-radius': '20px', 'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)'},
        
        config= {'displaylogo': False}),

    
    dcc.Graph(
        id= 'duration_vs_views',
        figure= duration_vs_views.update_layout(width= N_WIDTH,
                                                height= N_HEIGHT - DISTANCE),
        
        style= {'position': 'relative', 'display': 'inline-block',
                'bottom': f'{(N_HEIGHT + 2) - DISTANCE * 2}px', 'right': f'{100 + DISTANCE * 2}px',
                'padding':'5px', 'border-radius': '20px', 'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)'},
        
        config= {'displaylogo': False}),
    
    
    html.Div(["*Double click on legend buttons to isolate lines and bars."],
             style= {'position': 'relative', 'height': '20px', 'right': f'{L_WIDTH / 1.7}px',
                     'bottom': f'{N_HEIGHT - (DISTANCE * 5)}px', 'display': 'inline-block'}),
    
    
    dcc.Graph(
        id= 'video_stats_growth_per_time',
        figure= video_stats_growth_per_time.update_layout(width= L_WIDTH + DISTANCE,
                                                          height= N_HEIGHT),
    
        style= {'position': 'relative', 'bottom': f'{N_HEIGHT - (4 * DISTANCE)}px',
                'padding':'5px', 'border-radius': '20px',
                'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)',
                'display': 'inline-block', 'left': 'hi'},
    
        config= {'displaylogo': False}),

    
    dcc.Graph(
        id= 'video_stats_per_tag',
        figure= video_stats_per_tag.update_layout(width= L_WIDTH + DISTANCE,
                                                          height= N_HEIGHT),
    
        style= {'position': 'relative', 'bottom': f'{N_HEIGHT - (DISTANCE * 6)}px',
                'padding':'5px', 'border-radius': '20px',
                'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)',
                'display': 'inline-block', 'left': 'hi'},
    
        config= {'displaylogo': False}),
    
    
    dcc.Graph(
        id= 'likes_vs_views',
        figure= likes_vs_views.update_layout(width= L_WIDTH + DISTANCE,
                                                          height= N_HEIGHT),
    
        style= {'position': 'relative', 'bottom': f'{N_HEIGHT - (DISTANCE * 8)}px',
                'padding':'5px', 'border-radius': '20px',
                'box-shadow': '0 3px 5px rgba(0, 0, 0, 0.3)',
                'display': 'inline-block'},
    
        config= {'displaylogo': False}),
    
    
    html.Div(["By: Muhammed Ahmed Abd-Al-Aleam Elsayegh", html.Br(),
                 f"Last update: {TODAY}"],
                style= {'background-color': '#ededed', 'position': 'relative',
                        'padding': '3px', 'bottom' :'350px'})])
# ---------------------------------------------------------------