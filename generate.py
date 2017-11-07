import tracery
from tracery.modifiers import base_english

rules = {
        'story': '#origin##prelude#\n#journies#\n#end#.',
        'origin': '#age.capitalize# #sage1# #sage2#, a man from #town#, who was a #profession#, was #traveling# #across# #pos# #creek#, and #forgot# #destination#.\n',
        'age': ['In the time of', 'During the era of', 'During the rule of'],
        'sage1': ['Jin', 'Han', 'Li', 'Zhang', 'Zong', 'Kong', 'Sun', 'Ru'],
        'sage2': ['Wuling', 'Sima', 'Hongsi', 'Mazi', 'Jingran', 'Wuling'],
        'town': ['Taizhong','Jishi','Beifa','Honglu','Qinglin'],
        'profession': ['fisherman', 'physician', 'scholar', 'teacher','minister', 'warrior', 'disciple', 'poet', 'scribe', 'emperor', 'monk'],
        'traveling':['traveling','walking','traversing','wandering','passing', 'trekking', 'voyaging'],
        'across': ['across', 'down', 'up', 'through', 'along', 'beside' ,'near'],
        'pos': ['the edge of a', 'a', 'the corner of a', 'a distance from a'],
        'creek': ['creek', 'river', 'cavern', 'mountain', 'lake', 'forest', 'cave'],
        'type': ['peach blossom', 'forgotten', 'barren', 'lush', 'red', 'green', 'looming', 'distant'],
        'forgot': ['forgot the distance of the', 'forgot the', 'forgot the way to the'],
        'destination':['route', 'destination', 'path'],
        'prelude': 'He suddenly chanced upon a #type# #creek#, and found it #strange#.\nHe continued onwards, wanting to find the way out.',
        'strange': ['bizzare', 'strange', 'mystical', 'wonderful','calming'],
        'journey': ['#posn# #creek#, he got to a #creek#.', 'There #was# a #exit# in the #creek#, and so he #went#.', 'There #was# a #exit# in the #creek#, and #description#.', 'After #steps#, it suddenly #opened#.', 'The #ground# was #flat#, and #description#.', 'There he met a group of #people#, who were #profession#s and they #action#.', 'He #slept# for #number# days.'],
        'was': ['was', 'he found', 'he stumbled upon', 'he discovered', 'hidden, was', 'forgotten, was'],
        'slept': ['slept', 'meditated', 'danced', 'wrote poems', 'sung songs', 'prayed', 'thought', 'ascended'],
        'journies': ['#journey#\n#journies#', '#journey#\n#journies#', '#journey#\n#journies#', '#journey#\n#journies#\n#journey#','#journey#', '#journey#\n#journies#', '#journey#\n#journies#\n#journies#'],
        'posn': ['At the end of the', 'In the', 'Within the', 'Near the', 'Somewhere in the', 'Below the', 'Above the'],
        'exit': ['small hole', 'crevice', 'door', 'small opening', 'gaping hole', 'entrance', 'opening'],
        'went': ['went in', 'stepped in', 'crawled in', 'followed it'],
        'description': ['there was light', 'it invited him', 'it was moist','there was music', 'there was wind', 'it called him', 'it whispered', 'it was #flat#', 'it had sharp edges'],
        'number': ['thirty', 'one hundred', 'a thousand', 'three', 'twelve', 'four', 'six', 'forty'],
        'steps': ['a few steps', 'some distance', 'some time', 'a jump', '#number# steps', 'a mile', 'a moment'],
        'opened': ['closed', 'opened', 'rolled open', 'shook open', 'sung opened', 'disappeared', 'vanished', 'was forgotten'],
        'ground': ['ground','floor', 'ceiling', 'wall', 'air'],
        'flat' : ['flat', 'rough', 'heavy', 'light', 'soft', 'unstable', 'loud'],
        'people' : ['cave dwellers', 'dwarves', 'giants', 'fairies', 'dogs', 'cats', 'people', 'children', 'angels', 'spirits'],
        'action': ['greeted him', 'welcomed him', 'fed him', 'chased him', 'dressed him', 'washed him', 'hugged him', 'jumped him', 'asked him for the time', 'asked him what era it was', 'asked him where the #creek# was', 'asked him where the #exit# was', 'asked him if he was a #profession#'],
        'end': '#thereupon.capitalize# he left, mapping his way out.\nHe went to see the governor, and the governor sent people to follow his trail. But none could find the way.\n#sage1# #sage2# was a noble #profession# who heard of this and set out for it, but with no result; he #died#.\nAfter that, #concl#',
        'thereupon': ['after that', 'thereupon', 'after a while', 'after #number# days', 'after #number# years', 'quickly'],
        'died': ['died of illness', 'fell to his death', 'died in his sleep', 'died of poison', 'was murdered', 'was killed by the #people#', 'disappeared', 'vanished'],
        'concl': ['there were none who inquired about it', 'it was forgotten', 'it was lost', 'it was left alone', 'there were no more attempts','there were none who pursued further','there was no further attempt']
        }

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
story = grammar.flatten("#story#")
print story

with open('story.txt', 'a') as w:
    w.write('\n' + story + '\n')
