#argparse reference!
#from claude
"""
parser.add_argument(
    "name",              # positional: just the name
    "--name",            # optional: with dashes
    "-n", "--name",      # optional: short + long form

    # --- TYPE & VALUE ---
    type=int,            # convert input to int (or float, Path, etc.)
    default=5,           # value if argument not provided
    const=10,            # value used with nargs='?' when flag present but no value given
    choices=[1, 2, 3],   # restrict to specific values
    
    # --- HOW MANY VALUES ---
    nargs=3,             # exactly 3 values
    nargs='?',           # 0 or 1 value
    nargs='*',           # 0 or more values (returns list)
    nargs='+',           # 1 or more values (returns list)
    
    # --- BEHAVIOR ---
    action="store_true",   # sets True if flag present, False if not
    action="store_false",  # opposite
    action="append",       # each use appends to a list
    action="count",        # counts how many times flag is used (-vvv = 3)
    required=True,         # forces optional argument to be required
    
    # --- DISPLAY ---
    help="description shown in --help",
    metavar="FILENAME",    # name shown in --help instead of dest name
    dest="output_file",    # what attribute name to use on args object
)

"""