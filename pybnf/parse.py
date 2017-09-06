
import pyparsing as pp
import re

def parse(s):

    equals = pp.Suppress('=')
    comment = pp.Suppress(pp.ZeroOrMore('#' - pp.ZeroOrMore(pp.Word(pp.alphanums))))
    #set up multiple grammars

    #single str value 
    strkeys = pp.oneOf('bng_command job_name', caseless=True)
    string = pp.Word(pp.alphas)
    strgram = strkeys - equals - string -comment
    
    #single num value
    numkeys = pp.oneOf('verbosity parallel_count seed delete_old_files max_generations population_size smoothing min_objfunc_value objfunc extra_weight swap_rate max_parents force_different_parents keep_parents divide_by_init log_transform_sim_data standardize_sim_data standardize_exp_data', caseless=True)
    num = pp.Word(pp.nums)
    numgram = numkeys - equals - num - comment
    
    #multiple str value
    strskeys = pp.oneOf('output_dir model exp_file', caseless=True)
    strings = pp.OneOrMore(pp.Word(pp.alphas))
    strsgram = strskeys - equals - strings -comment
    
    #multiple str and num value
    strnumkeys = pp.oneOf('mutate random_var lognormrandom_var loguniform_var', caseless=True)
    varnums = pp.OneOrMore(strings - pp.Word(pp.nums) - pp.Word(pp.nums))
    strnumgram = strnumkeys - pp.ZeroOrMore(equals) - varnums -comment
    
    #static_list_var grammar
    slvkey = pp.oneOf('static_list_var', caseless=True)
    slvgram = slvkey - equals - string - pp.OneOrMore(pp.Word(pp.nums)) -comment
    
    #check each grammar and output somewhat legible error message 
    line = (strgram | numgram | strsgram | strnumgram | slvgram).parseString(s, parseAll=True).asList() 

    
    return line
    
def ploop(path):  # parse loop
    d = {}
    
    with open(path, "r") as infile:
        for i,line in enumerate(infile):
            if re.match('\s*$', line) or re.match('\s*#', line):
                continue
            try:
                l = parse(line)
                print (l)
                key = l[0]
                values = l[1:]
                d[key] = values #set key to values
            except:
                message = "misconfigured parameter '%s' at line: %s"%(line.strip(), i)
 #               print (message)
                raise Exception(message)
                
    return d

class IllegalParamException(Exception):
    def __init__(self, value):
        print (self.message)