# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 17:56:37 2020

@author: User
"""

#import pygal
#
#gauge=pygal.Gauge()
#
#gauge.title = 'Gauge Chart'     
#  
#gauge.range = [0, 5000] 
#  
## Random data 
#gauge.add('A', 3000) 
#gauge.add('B', 2000) 
#gauge.add('C', 3500) 
#gauge.render_to_file('gauge.svg')


# importing pygal 
import pygal 
  
# creating the chart object 
Solid_Gauge = pygal.SolidGauge(inner_radius = 0.75,  
                               half_pie = True) 
  
# naming the title 
Solid_Gauge.title = 'SCP(Psi) Pressure Monitoring'     
  
# Random data 
Solid_Gauge.add('KINDP-A101', [{'value': 300, 'max_value': 2000}]) 
Solid_Gauge.add('KINDP-A104', [{'value': 520, 'max_value': 700}]) 
Solid_Gauge.add('KINDP-A105', [{'value': 75, 'max_value': 2000}]) 
  
Solid_Gauge.render_to_file('gauge.svg')

