from bokeh.plotting import figure, output_notebook, show
import pandas as pd

output_notebook()

d = { 
'x': [1, 2, 3, 4, 5]
 ,  
'y': [1, 2, 3, 4, 5]
 }

df = pd.DataFrame(data=d)

p = figure(title="simple line example", x_axis_label='x', y_axis_label='y')

p.line(source= df ,x='x', y='y', legend_label="Temperature", line_width=2)

show(p)


