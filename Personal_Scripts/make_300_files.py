import random
filenames = ['anise', 'pardon', 'basin', 'coral', 'drake', 'trench', 'twins', 'cash', 'safe', 'divide', 'hall', 'dime', 'local', 'atom', 'ideal', 'medal', 'thrill', 'voting', 'union', 'length', 'crayon', 'mother', 'lye', 'phrase', 'mime', 'grace', 'larder', 'toe', 'poppy', 'river', 'edge', 'pirate', 'beech', 'export', 'key', 'mail', 'tour', 'draft', 'condor', 'patron', 'bin', 'nasal', 'buyer', 'zen', 'obi', 'guava', 'ramen', 'weasel', 'mom', 'tensor', 'charm', 'havoc', 'tummy', 'egg', 'gutter', 'stack', 'almond', 'thing', 'smolt', 'ark', 'dress', 'jack', 'icing', 'organ', 'belfry', 'raven', 'ant', 'killer', 'sorrow']
ext = ['exe', 'pdf', 'jpg', 'mp4', 'docx', 'zip', 'txt']
print(filenames)
print(ext)

   


for i in range(300):
    random_name = random.choice(filenames)
    random_ext = random.choice(ext)
    random_num = random.randint(1000,9999)
    with open(f"{random_name}{random_num}.{random_ext}","w"):
        pass
        
    
    