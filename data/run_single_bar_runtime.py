from bokeh.models import FactorRange
from bokeh.palettes import TolPRGn4
from bokeh.plotting import figure, show
from bokeh.palettes import Bright6

hashes =('poseidon', 'poseidon2', 'monolith', 'griffin', 'arion', 'anemoi', 'mimc','rescue_prime','gmimc','neptune')

libs = (
    ("poseidon", "circom-snarkjs"), ("poseidon", "plonky2"), ("poseidon", "noir"),("poseidon", "halo2-kzg/ pasta"),
    ("poseidon2", "circom-snarkjs"), ("poseidon2", "plonky2"), ("poseidon2", "noir"),("poseidon2", "boojum"),
    ("monolith", "plonky2"),
    ("griffin", "plonky2"), ("griffin", "noir"),
    ("arion", "plonky2"),
    ("anemoi", "plonky2"),
    ("mimc", "circom-snarkjs"), ("mimc", "plonky2"), ("mimc", "halo2-kzg/ pallas"),("mimc", "halo2-kzg/ vesta"), ("mimc", "noir"),
    ("rescue_prime", "plonky2"),
    ("gmimc", "circom-snarkjs"),
    ("neptune", "circom-snarkjs"),
)

fill_color, line_color = TolPRGn4[2:]

p = figure(x_range=FactorRange(*libs), height=500, width = 1200, 
           background_fill_color="#fafafa", title="Runtime/ ms, for Hash Functions/ Libs")

runtime = [0.44, 0.016, 0.557, 0.060,  0.43,  0.005, 0.530, 0.037, 0.007,  0.040,  0.555, 0.056, 0.025,0.49, 0.023,0.055, 0.045, 0.512,0.031, 0.59,  0.47  ]
ram = [192020480, 3522560, 219629158, 4341760, 174446976,3571712, 180402586, 7389184,3571712,18857984, 180631962, 32358400, 18939904,219758592, 7503872, 3981312, 3997696,172764365, 3670016,202266560, 175544640  ]

p.vbar(x=libs, top=runtime, width=0.8,
       fill_color=fill_color, fill_alpha=0.8, line_color=line_color, line_width=1.2)

min_runtime = [0.016, 0.005, 0.007, 0.040, 0.056, 0.025, 0.023,0.031, 0.59,  0.47 ]
min_ram = [13, 9, 13, 14]


p.line(x=hashes, y=min_runtime, color=line_color, line_width=3)
p.scatter(x=hashes, y=min_runtime, size=10,
          line_color=line_color, fill_color="white", line_width=3)

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)