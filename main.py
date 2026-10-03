
from kivy.app import App
from kivy.clock import Clock
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.progressbar import ProgressBar
from kivy.graphics import Color, RoundedRectangle
import random

WORDS = [('abgesehen', 'apart from'), ('abitur', 'high school diploma'), ('abschließende', 'final'), ('abschlussklassen', 'graduating classes'), ('absicht', 'intention'), ('ach', 'oh'), ('achtung', 'attention'), ('agiert', 'acts'), ('akkus', 'batteries'), ('aktualität', 'current events'), ('akzeptieren', 'accept'), ('albtraum', 'nightmare'), ('allem', 'above all'), ('allmählich', 'gradually'), ('allzu', 'too much'), ('also', 'so'), ('anblick', 'sight'), ('anfangen', 'to start'), ('angaben', 'information'), ('angeber', 'show-off'), ('angeblich', 'allegedly'), ('angegeben', 'specified'), ('angekom', 'arrived'), ('angenehm', 'pleasant'), ('angepasst', 'adapted'), ('angerempelt', 'bumped into'), ('angriff', 'attack'), ('anhören', 'to listen'), ('ankunft', 'arrival'), ('annahme', 'assumption'), ('ansagen', 'announcement'), ('ansehen', 'to look at'), ('anzeige', 'report'), ('anzuse', 'to be seen'), ('arbeitsgemeinschaft', 'working group'), ('arm', 'poor'), ('armreife', 'armbands'), ('atmen', 'to breathe'), ('atmet', 'breathes'), ('auch', 'also'), ('auf', 'on'), ('aufenthalts', 'residence'), ('aufenthaltsraum', 'common room'), ('aufführung', 'performance'), ('aufgaben', 'tasks'), ('aufgeregt', 'excited'), ('aufgerissenen', 'torn open'), ('aufgesetzt', 'put on'), ('aufkom', 'emerges'), ('auflage', 'edition'), ('aufmerksam', 'attentive'), ('aufmerksamkeit', 'attention'), ('aufregung', 'excitement'), ('aufrichten', 'to straighten up'), ('aufzunehmen', 'to record'), ('augen', 'eyes'), ('augenbli', 'moment'), ('augenblick', 'eye contact'), ('augenfarbe', 'eye color'), ('augenlids', 'eyelid'), ('ausgangspunkt', 'declared aim'), ('ausgehen', 'to go out'), ('ausgängen', 'exits'), ('auskosten', 'to enjoy'), ('aussage', 'statement'), ('aussehen', 'appearance'), ('ausweichen', 'to avoid'), ('auswendig', 'by heart'), ('autofah', 'driving'), ('autofahrer', 'driver'), ('außerdem', 'besides'), ('ayschemut', 'Ayschemut'), ('aysches', 'Aysches'), ('bahn', 'train'), ('bahngleis', 'train track'), ('bandenkriegen', 'gang wars'), ('bankangestellten', 'bank clerk'), ('bankraubes', 'bank robbery'), ('bankschalter', 'teller'), ('banküberfall', 'bank heist'), ('banküberfalls', 'Baumgarten'), ('baumgarten', 'Bavaria'), ('bayern', 'commissioner'), ('beauftragte', 'thanked'), ('bedankt', 'need'), ('bedarf', 'to mean'), ('bedeuten', 'threatened'), ('bedroht', 'impressed'), ('beeindruckt', 'to be located'), ('befinden', 'to question'), ('befragen', 'questioned'), ('befragt', 'to meet'), ('begegnen', 'to begin'), ('beginnen', 'begin  '), ('begleite', 'accompany  '), ('begreift', 'understands  '), ('begründen', 'justify  '), ('begrüßt', 'greets  '), ('behält', 'keeps  '), ('beiden', 'both  '), ('beigelegte', 'enclosed  '), ('bein', 'leg  '), ('bekommst', 'you get  '), ('belasten‘', 'stress  '), ('bellt', 'barks  '), ('bemerkt', 'notices  '), ('beobachtet', 'observes  '), ('ber', 'mountain  '), ('bereits', 'already  '), ('berufli', 'professional  '), ('berufstätig', 'employed  '), ('berufswunsch', 'career aspiration  '), ('beruhigen', 'calm  '), ('beruhigt', 'calmed  '), ('bescheid', 'notification  '), ('beschließt', 'decides  '), ('beschreiben', 'describe  '), ('beschreibung', 'description  '), ('besitzt', 'owns  '), ('besoffen', 'drunk  '), ('besonders', 'especially  '), ('besorgt', 'concerned  '), ('besser', 'better  '), ('bestellung', 'order  '), ('bestimmt', 'certain  '), ('besuch', 'visit  '), ('betritt', 'enters  '), ('betrunken', 'drunk  '), ('betrunkener', 'drunk person  '), ('beugen', 'bend  '), ('beunruhigen', 'worry  '), ('bewegen', 'move  '), ('bewegt', 'moved  '), ('bewegung', 'movement  '), ('beziehung', 'relationship  '), ('bezirk', 'district  '), ('bier', 'beer  '), ('bierkrug', 'beer mug  '), ('bierkrüge', 'beer mugs  '), ('bilder', 'pictures  '), ('bildet', 'forms  '), ('bildungseinrichtungen', 'educational institutions  '), ('bisher', 'so far  '), ('bist', 'are  '), ('bleiben', 'stay  '), ('bleibt', 'stays  '), ('bleme', 'blemishes  '), ('blick', 'glance  '), ('blickt', 'looks  '), ('blitzschnell', 'lightning-fast  '), ('blonden', 'blonde  '), ('bloß', 'just  '), ('bluse', 'blouse  '), ('blutet', 'bleeds  '), ('boden', 'floor  '), ('bol', 'bowl  '), ('borgne', 'one-eyed  '), ('bracht', 'brought  '), ('breite', 'width  '), ('brennen', 'burn  '), ('bringen', 'bring  '), ('brote', 'breads  '), ('brust', 'chest  '), ('brutalen', 'brutal  '), ('buchgestaltung', 'book design  '), ('bun', 'co  '), ('bunte', 'colorful  '), ('bzw', 'respectively  '), ('bückt', 'bends  '), ('bürgersteig', 'sidewalk  '), ('büroangestellte', 'office worker  '), ('cdspie', 'CD game  '), ('chen', 'little  '), ('chrlich', 'honest  '), ('cke', 'thick  '), ('dabei', 'with it  '), ('damit', 'with it  '), ('daran', 'about it  '), ('darauf', 'on it  '), ('daraus', 'from it  '), ('darf', 'may  '), ('darüber', 'about it  '), ('dasselbe', 'the same  '), ('dateien', 'files  '), ('dauert', 'lasts  '), ('davon', 'of it  '), ('davor', 'before it  '), ('dazu', 'for it  '), ('deckblatt', 'cover page  '), ('dein', 'your  '), ('dem', 'the  '), ('denn', 'because  '), ('dersehen', 'to see  '), ('des', 'of  '), ('deshalb', 'therefore  '), ('deutschvorkenntnissen', 'German prior knowledge  '), ('dias', 'slides  '), ('dichtes', 'dense  '), ('dienststelle', 'office  '), ('diese', 'these  '), ('dir', 'to you  '), ('doch', 'but  '), ('dra', 'there  '), ('drinnen', 'inside  '), ('drohend', 'threatening  '), ('drucklegung', 'printing  '), ('drüben', 'over there  '), ('drückt', 'presses  '), ('durch', 'through  '), ('durcheinander', 'confused  '), ('durst', 'thirst  '), ('dürfen', 'may  '), ('dürfte', 'would  '), ('eben', 'just  '), ('ecke', 'corner  '), ('ehemaligen', 'former  '), ('eigenen', 'own  '), ('eigentlich', 'actually  '), ('eilen', 'hurry  '), ('eilig', 'urgent  '), ('einfach', 'simple  '), ('einfahrt', 'driveway  '), ('einfluss', 'influence  '), ('eingegangenen', 'received  '), ('eingeladen', 'invited  '), ('eingescannt', 'scanned  '), ('eingestellt', 'set  '), ('einige', 'some  '), ('einkauf', 'purchase  '), ('einlegen', 'insert  '), ('einsteigen', 'get in  '), ('einwilligung', 'consent  '), ('einzelkind', 'only child  '), ('einzeln', 'individual  '), ('eiskalter', 'ice cold  '), ('elend', 'miserable  '), ('eltern', 'parents  '), ('empfangen', 'receive  '), ('endete', 'ended  '), ('energisch', 'energetic  '), ('eng', 'narrow  '), ('enthält', 'contains  '), ('entscheidenden', 'decisive  '), ('entschließen', 'decide  '), ('entschuldigen', 'apologize  '), ('entsetzt', 'horrified  '), ('enttäuschen', 'disappoint  '), ('enttäuscht', 'disappointed  '), ('ereignis', 'event  '), ('erfahren', 'learn  '), ('erfolg', 'success  '), ('erfreuliche', 'pleasant  '), ('erfährt', 'finds out  '), ('erfühlt', 'felt  '), ('ergeben', 'results  '), ('ergibt', 'results in  '), ('erinnern', 'remember  '), ('erinnert', 'remembers  '), ('erkennen', 'recognize  '), ('erlauben', 'allow  '), ('erleichtert', 'relieved  '), ('erloschen', 'extinguished  '), ('ermittlungen', 'investigations  '), ('ermuntert', 'encouraged  '), ('ernst', 'serious  '), ('erreichen', 'achieve'), ('erschrickt', 'frightened'), ('erschrocken', 'frightened'), ('erst', 'only'), ('erstaunt', 'astonished'), ('erwachen', 'Awakening'), ('erwacht', 'awakened'), ('erwartet', 'expected'), ('erzähle', 'Tell me'), ('erzählen', 'Tell'), ('erzählt', 'narrated'), ('etwa', 'about'), ('euch', 'you'), ('europäischer', 'European'), ('fabrikgebäude', 'Factory building'), ('fach', 'Subject'), ('fachhochschule', 'University of Applied Sciences'), ('fahrstuhl', 'Elevator'), ('fahrstuhltür', 'Elevator door'), ('fall', 'Case'), ('falls', 'if'), ('fandest', 'You found'), ('fast', 'almost'), ('fasziniert', 'fascinated'), ('fen', 'Fen'), ('fentlich', 'Public'), ('fest', 'Fixed'), ('festgebrannt', 'Burned'), ('festgehalten', 'held'), ('festhalten', 'Hold on'), ('fete', 'party'), ('fey', 'Fey'), ('flüssigkeit', 'Liquid'), ('forstwirtschaft', 'Forestry'), ('fort', 'Away'), ('freudig', 'joyful'), ('freundes', 'Friend'), ('freundinan', 'Girlfriend'), ('freut', 'pleased'), ('friert', 'freezes'), ('früher', 'Previous'), ('frühlingstag', 'Spring Day'), ('furchtbarer', 'more terrible'), ('fußgänger', 'Pedestrians'), ('fußgängers', 'pedestrians'), ('fähigkeit', 'Ability'), ('fälle', 'Cases'), ('fällen', 'Cases'), ('fällt', 'falls'), ('fängnisses', 'Catch'), ('fängt', 'catches'), ('fühle', 'feel'), ('fühlen', 'feel'), ('fühlt', 'feels'), ('führt', 'leads'), ('fürchtet', 'fears'), ('füreinander', 'for each other'), ('gab', 'gave'), ('gangsterrap', 'Gangster rap'), ('ganz', 'all'), ('gar', 'even'), ('gearbeitet', 'worked'), ('geboren', 'born'), ('gebrochen', 'broken'), ('gedanke', 'Thought'), ('gedanken', 'Thoughts'), ('gedroht', 'threatened'), ('gedruckt', 'Printed'), ('geduld', 'Patience'), ('gefahr', 'Danger'), ('gefangen', 'Caught'), ('gefasst', 'Caught'), ('gefällt', 'Like'), ('gefühl', 'Feeling'), ('gegangen', 'gone'), ('gegeben', 'given'), ('gegen', 'against'), ('gegend', 'Area'), ('gegeneinanderprallen', 'to collide with each other'), ('gegensei', 'Gegensei'), ('gegenüber', 'opposite'), ('geglaubt', 'believed'), ('geh', 'Go'), ('geheim', 'secret'), ('gehen', 'Go'), ('gehofft', 'hoped for'), ('geholfen', 'helped'), ('gehorchen', 'Obey'), ('geht', 'goes'), ('gehört', 'Heard'), ('geist', 'Spirit'), ('gekleideter', 'dressed'), ('geklärt', 'clarified'), ('gelassenen', 'Left'), ('gelaunt', 'in a good mood'), ('gelernt', 'learned'), ('gelesen', 'read'), ('gelingt', 'succeeds'), ('gelohnt', 'Worth it'), ('gelten', 'apply'), ('gelöst', 'Solved'), ('gemacht', 'made'), ('gemeinsam', 'together'), ('gen', 'Keywords'), ('genau', 'accurate'), ('genervt', 'Annoyed'), ('genießen', 'Enjoy'), ('genossen', 'Enjoyed'), ('gepackt', 'packed'), ('geplant', 'planned'), ('geprüft', 'checked'), ('gerechnet', 'calculated'), ('gerissen', 'ripped'), ('gerne', 'gladly'), ('gerät', 'device'), ('geräusch', 'noise'), ('geräusch', 'noise'), ('gesagt', 'said'), ('geschenk', 'gift'), ('geschenkartikel', 'gift item'), ('geschenkt', 'given'), ('geschlossene', 'closed'), ('geschwindigkeit', 'speed'), ('geschäft', 'business'), ('geschützt', 'protected'), ('gesehen', 'seen'), ('gesetzlich', 'legal'), ('gesicht', 'face'), ('gesichtsmaske', 'face mask'), ('gespenster', 'ghosts'), ('gestellt', 'placed'), ('gestoßen', 'bumped'), ('gesun', 'sung'), ('gesungen', 'sung'), ('getan', 'done'), ('gewesen', 'been'), ('gewinnen', 'to win'), ('gewissen’', 'certain'), ('gewonnene', 'won'), ('geworden', 'become'), ('gewähr', 'guarantee'), ('gewühl', 'bustle'), ('geäußert', 'expressed'), ('gibt', 'gives'), ('glas', 'glass'), ('glei', 'same'), ('gleichzeitig', 'simultaneously'), ('gleitet', 'glides'), ('gläsern', 'glassy'), ('goldenen', 'golden'), ('gott', 'god'), ('greifen', 'grab'), ('grinsen', 'grin'), ('gucken', 'look'), ('guckt', 'looks'), ('gymnasiums', 'high school'), ('hals', 'neck'), ('halter', 'holder'), ('haltestelle', 'bus stop'), ('handeln', 'act'), ('handelt', 'deals'), ('handlung', 'action'), ('hart', 'hard'), ('hat', 'has'), ('haut', 'skin'), ('hefti', 'booklet'), ('heftigen', 'intense'), ('heimfahrt', 'journey home'), ('hektisch', 'hectic'), ('hellwach', 'wide awake'), ('heraus', 'out'), ('herauskommen', 'come out'), ('herrlichen', 'splendid'), ('herrscht', 'prevalent'), ('herzlichkeit', 'affection'), ('hin', 'to'), ('hinaus', 'out'), ('hinweis', 'hint/highlight'), ('hoch', 'high'), ('hochbetrieb', 'high activity'), ('hof', 'yard'), ('hoffe', 'hope'), ('hoffentlich', 'hopefully'), ('hoffnung', 'hope'), ('hofft', 'hopes'), ('hundebesitzer', 'dog owner'), ('hunden', 'dogs'), ('hundertprozentig', 'hundred percent'), ('hustet', 'coughs'), ('hälfte', 'half'), ('hält', 'holds'), ('hältst', 'you hold'), ('hände', 'hands'), ('händen', 'hands'), ('hätte', 'would have'), ('häufchen', 'little pile'), ('höheren', 'higher'), ('hör', 'hear'), ('hörerlebnis', 'listening experience'), ('hörst', 'you hear'), ('hört', 'hears'), ('ihm', 'him'), ('ihn', 'him'), ('ihnen', 'them'), ('ihrem', 'their'), ('ihren', 'theirs'), ('ihres', 'theirs'), ('illustrationen', 'illustrations'), ('inder', 'Indian'), ('informationen', 'information'), ('inhalt', 'content'), ('ins', 'into'), ('inzwischen', 'meanwhile'), ('irgendwo', 'somewhere'), ('irren', 'err'), ('irrt', 'errs'), ('irrtum', 'error'), ('isdieen', 'is this'), ('japaner', 'Japanese'), ('jedes', 'everybody'), ('jemand', 'someone'), ('jugendhorel', 'youth whore'), ('jugendhotels', 'youth whore'), ('junge', 'boy'), ('junger', 'young'), ('kannten', 'knew'), ('kapitel', 'chapter'), ('kauft', 'buys'), ('kaum', 'hardly'), ('keiten', '-ities'), ('kenne', 'know'), ('kennen', 'know'), ('kennst', 'know (informal you)'), ('kennt', 'knows'), ('kerl', 'guy'), ('kichern', 'giggle'), ('kisch', 'shush'), ('klassenarbeit', 'class test'), ('klassenfahrt', 'class trip'), ('klassenkameraden', 'classmates (male or mixed)'), ('klassenkameradin', 'classmate (female)'), ('klausur', 'exam'), ('kleidungsstücke', 'articles of clothing'), ('kleinigkeit', 'trifle'), ('klingelt', 'rings'), ('kommen', 'come'), ('konnte', 'could'), ('kontostand', 'account balance'), ('kontrollieren', 'check'), ('kopfhörer', 'headphones'), ('kopfkis', 'pillow for head'), ('kopfschmerzen', 'headache'), ('krach', 'noise'), ('krach‘', 'noise (colloquial)'), ('kraft', 'strength'), ('kreutzer', 'kreutzer (old currency)'), ('kreuzen', 'cross'), ('krimi', 'crime'), ('kriminalhaupt', 'detective inspector'), ('krimineller', 'criminal'), ('kurzes', 'short'), ('kämpfen', 'fight'), ('kästchen', 'little box'), ('käuflich', 'for sale'), ('können', 'can'), ('könnte', 'could'), ('lachen', 'laugh'), ('lacht', 'laughs'), ('lade', 'load'), ('ladegerät', 'charger'), ('laden', 'load'), ('ladend', 'loading'), ('landeskundliche', 'regional/cultural'), ('lange', 'long'), ('lass', 'let'), ('leben', 'live'), ('lebhaften', 'lively'), ('leere', 'empty'), ('lege', 'put'), ('legen', 'lay'), ('legt', 'lays'), ('lehrern', 'teachers'), ('leid', 'sorry'), ('leidenschaft', 'passion'), ('leider', 'unfortunately'), ('leine', 'leash'), ('leise', 'quiet'), ('leiser', 'quieter'), ('leistungs', 'performance'), ('leite', 'lead'), ('leitet', 'leads'), ('lektorat', 'editing'), ('ler', 'study (abbreviated)'), ('leser', 'reader'), ('leserinnen', 'female readers'), ('letzten', 'last'), ('leuchten', 'shine'), ('lextraprodukte', 'extra products'), ('lich', 'light'), ('liebespaar', 'couple in love'), ('liebt', 'loves'), ('lied', 'song'), ('liedes', 'song’s'), ('liegen', 'lie'), ('liegt', 'lies'), ('lipps', 'lips'), ('lle', 'lle (abbreviation or typo)'), ('locken', 'curls'), ('lose', 'loose'), ('losgehen', 'start'), ('luft', 'air/luck'), ('luxuskarosse', 'luxury car'), ('lächeln', 'smile'), ('lächelt', 'smiles'), ('längst', 'long ago'), ('lässt', 'lets'), ('läuft', 'runs'), ('machst', 'do (you)'), ('macht', 'do/does'), ('maisonne', "maisonne (likely 'maison' misspelled)"), ('mannes', "man's"), ('maskier', 'mask'), ('maskierte', 'masked'), ('maskierter', 'masked'), ('maß', 'measure'), ('mehrere', 'several'), ('meinst', 'mean'), ('meist', 'often'), ('melden', 'report'), ('menschenmenge', 'crowd'), ('merken', 'notice'), ('miteinander', 'together'), ('mitge', 'with gone'), ('mitgebracht', 'brought along'), ('mitglied', 'member'), ('mithohr', 'overhear'), ('mittagssonne', 'midday sun'), ('mittelpunkt', 'center'), ('mitternacht', 'midnight'), ('mittlerweile', 'by now'), ('modische', 'fashionable'), ('mond', 'moon'), ('mund', 'mouth'), ('mut', 'courage'), ('möchte', 'would like'), ('möglich', 'possible'), ('möglichkeit', 'possibility'), ('müdigkeit', 'tiredness'), ('mündlichen', 'oral'), ('müsste', 'would have to'), ('nachdem', 'after'), ('nachdenklich', 'thoughtful'), ('nachhaltiger', 'more sustainable'), ('nachmittag', 'afternoon'), ('nachsehen', 'check'), ('namen', 'names'), ('neben', 'next to'), ('nebeneinander', 'side by side'), ('nebenstraße', 'side street'), ('nehmen', 'take'), ('nen', 'a'), ('neugierig', 'curious'), ('nichts', 'nothing'), ('niemand', 'nobody'), ('nimmt', 'takes'), ('noch', 'still'), ('nutzerhinweise', 'user notes'), ('nutzung', 'use'), ('oberkörper', 'torso'), ('obersten', 'top'), ('oberstudienrat', 'senior teacher'), ('offen', 'open'), ('ohr', 'ear'), ('ons', 'ons (unclear context)'), ('oper', 'opera'), ('paar', 'couple'), ('pas', 'no'), ('passanten', 'passersby'), ('passen', 'fit'), ('passieren', 'happen'), ('passt', 'fits'), ('personalien', 'personal details'), ('personals', "staff's"), ('pfeifen', 'whistles'), ('planmäßige', 'scheduled'), ('plötz', 'sudden'), ('polizeibeamte', 'police officer  '), ('pralinen', 'chocolates  '), ('privatklinik', 'private clinic  '), ('proben', 'samples  '), ('prospekte', 'brochures  '), ('protokoll', 'protocol  '), ('radfah', 'cycling  '), ('radfahrern', 'cyclists  '), ('rand', 'edge  '), ('rappern', 'rappers  '), ('rast', 'rest  '), ('recht', 'right  '), ('rede', 'speech  '), ('reden', 'speeches  '), ('redet', 'talks  '), ('referenzrahmen', 'frame of reference  '), ('regie', 'direction  '), ('regisseur', 'director  '), ('regnen', 'rain  '), ('reihe', 'row  '), ('reihenfolge', 'sequence  '), ('reisenden', 'traveler  '), ('rennt', 'runs  '), ('richtet', 'aims  '), ('riecht', 'smells  '), ('ringt', 'wrestles  '), ('ruft', 'calls  '), ('rutscht', 'slips  '), ('rätsel', 'riddle  '), ('rücken', 'back  '), ('sache', 'thing  '), ('sag', 'say  '), ('sanft', 'gentle  '), ('satz', 'sentence  '), ('schaffe', 'create  '), ('schaften', 'connections  '), ('schaufenster', 'shop window  '), ('schaut', 'watches  '), ('schen', 'give  '), ('schenk', 'gift  '), ('scherze', 'jokes  '), ('schicht', 'shift  '), ('schickt', 'sends  '), ('schießt', 'shoots  '), ('schlagen', 'hit  '), ('schlank', 'slim  '), ('schlecht', 'bad  '), ('schlechter', 'worse  '), ('schlechtes', 'bad (neuter)  '), ('schließt', 'closes  '), ('schlimmste', 'worst  '), ('schlägt', 'hits  '), ('schmal', 'narrow  '), ('schmalen', 'narrow (plural)  '), ('schmeckt', 'tastes  '), ('schmitz', 'Schmitz  '), ('schmuck', 'jewelry  '), ('schnauze', 'snout  '), ('schneiderei', 'tailoring  '), ('schnellen', 'quick  '), ('schock', 'shock  '), ('schon', 'already  '), ('schreck', 'fright  '), ('schreibung', 'writing  '), ('schreit', 'screams  '), ('schrift', 'script  '), ('schriftliche', 'written  '), ('schritte', 'steps  '), ('schritten', 'stepped  '), ('schuhe', 'shoes  '), ('schulabschluss', 'school graduation  '), ('schulen', 'schools  '), ('schulkameraden', 'classmates  '), ('schulkinder', 'school children  '), ('schulschluss', 'end of school  '), ('schulter', 'shoulder  '), ('schultern', 'shoulders  '), ('schusswaffe', 'firearm  '), ('schwarzen', 'black  '), ('schwarzer', 'black (masculine)  '), ('schweigen', 'silence  '), ('schweigt', 'silent  '), ('schöneberger', 'Schöneberger  '), ('schüler', 'student  '), ('schülerinnen', 'female students  '), ('schülern', 'students  '), ('schüttelt', 'shakes'), ('sehe', 'see'), ('sein', 'be'), ('serviert', 'served'), ('setzen', 'set'), ('setzt', 'sets'), ('sich', 'oneself'), ('siehe', 'see'), ('sieht', 'sees'), ('siert', 'decorates'), ('silberne', 'silver'), ('sind', 'are'), ('sinn', 'sense'), ('sofort', 'immediately'), ('sogar', 'even'), ('solche', 'such'), ('soll', 'shall'), ('sollen', 'should'), ('sommertag', 'summer day'), ('sonne', 'sun'), ('sonniger', 'sunny'), ('sonst', 'otherwise'), ('sonstigen', 'other'), ('sorge', 'care'), ('sorgenvoll', 'worried'), ('soweit', 'as far as'), ('spannende', 'exciting'), ('spazieren', 'walk'), ('spaziergang', 'walk'), ('spaziergängern', 'walkers'), ('speisekarte', 'menu'), ('spenster', 'spirit'), ('spielen', 'play'), ('sport', 'sports'), ('sporthalle', 'gym'), ('sportverein', 'sports club'), ('springt', 'jumps'), ('spur', 'track'), ('spürt', 'feels'), ('stam', 'stem'), ('starrt', 'stares'), ('statt', 'instead'), ('stehe', 'stand'), ('steht', 'stands'), ('steigen', 'climb'), ('steigt', 'climbs'), ('stein', 'stone'), ('stelle', 'place'), ('stellt', 'places'), ('still', 'quiet'), ('stimme', 'voice'), ('stirn', 'forehead'), ('stockwerk', 'floor'), ('stoß', 'push'), ('strahlendes', 'radiant'), ('straßenseite', 'side of the street'), ('streichholz', 'match'), ('strengem', 'strict'), ('stärker', 'stronger'), ('stößt', 'pushes'), ('stück', 'piece'), ('stürmt', 'storms'), ('säurefreiem', 'acid-free'), ('tankstelle', 'gas station'), ('tastet', 'feels'), ('tatort', 'crime scene'), ('tauber', 'deaf'), ('teile', 'parts'), ('teilnehme', 'participate'), ('teilzunehmen', 'to participate'), ('theaterag', 'theater company'), ('tief', 'deep'), ('tiefen', 'depths'), ('titel', 'title'), ('tod', 'death'), ('ton', 'sound'), ('toningenieur', 'sound engineer'), ('tot', 'death'), ('tragen', 'carry'), ('trauerspiel', 'tragedy'), ('traurig', 'sad  '), ('traut', 'dares  '), ('treibt', 'drives  '), ('trennen', 'separate  '), ('tritt', 'steps  '), ('trocken', 'dry  '), ('trotz', 'despite  '), ('trägt', 'carries  '), ('tränen', 'tears  '), ('trösten', 'comfort  '), ('tun', 'do  '), ('turnhalle', 'gym  '), ('tut', 'does  '), ('täter', 'perpetrator  '), ('tätigkeit', 'activity  '), ('tödlich', 'deadly  '), ('tödlicher', 'more deadly  '), ('töten', 'kill  '), ('umarmt', 'hugs  '), ('umfahren', 'run over  '), ('umjedes', 'every  '), ('umschlaggestaltung', 'envelope design  '), ('umschlungen‘', 'embraced  '), ('umsetzung', 'implementation  '), ('umstände', 'circumstances  '), ('unangenehmes', 'unpleasant  '), ('unbekannte', 'unknown  '), ('unbekannten', 'unknowns  '), ('undeutlich', 'unclear  '), ('unfall', 'accident  '), ('ungleicher', 'unequal  '), ('ungläubig', 'unbelieving  '), ('unheimlichen', 'eerie  '), ('unrechtes', 'unjust  '), ('unruhig', 'restless  '), ('uns', 'us  '), ('unser', 'our  '), ('unten', 'below  '), ('unter', 'under  '), ('unterhalten', 'entertain  '), ('unterhaltsamen', 'entertaining  '), ('unterschrieben', 'signed  '), ('unterstreichen', 'underline  '), ('untersuchungen', 'investigations  '), ('ununterbrochen', 'continuously  '), ('urheberrechtlich', 'copyrighted  '), ('urhg', 'UrhG (German Copyright Act)  '), ('vak', 'vacant  '), ('ver', 'for  '), ('verabredeten', 'agreed  '), ('verabredung', 'appointment  '), ('verabschieden', 'say goodbye  '), ('verabschiedet', 'farewell  '), ('verabschiedung', 'farewelled  '), ('verbotenes', 'farewell  '), ('verbre', 'forbidden  '), ('verbringen', 'spread  '), ('verdacht', 'spend  '), ('verdächtigen', 'suspicion  '), ('vereinen', 'suspects  '), ('verfolgt', 'unite  '), ('verfügung', 'pursued  '), ('vergangenheit', 'disposal  '), ('vergessen', 'past  '), ('verglüht', 'forget  '), ('vergnüglichen', 'burns out  '), ('verheimlichen’', 'amusing  '), ('verkehr', 'hide  '), ('verkehrsgesellschaft', 'traffic  '), ('verlag', 'transport company  '), ('verlages', 'publisher  '), ('verlassen', 'publishing  '), ('verletzen', 'leave  '), ('verliebt', 'injure  '), ('verlinkt', 'in love  '), ('verloren', 'linked  '), ('verlässt', 'lost  '), ('vermitteln', 'leaves  '), ('verschaffen', 'mediate  '), ('verschoben', 'provide  '), ('verschweigen', 'postponed  '), ('verschwindet', 'conceal  '), ('versprechen', 'disappears  '), ('versteck', 'promise  '), ('verstehe', 'hideout  '), ('versteht', 'understand  '), ('versucht', 'understands  '), ('verteilt', 'tries'), ('vertraue', 'trust  '), ('vertrauen', 'trust  '), ('vertreibt', 'drives out  '), ('vertretung', 'representation  '), ('verwandte', 'relative  '), ('verwandtschaft', 'kinship  '), ('verzichtet', 'gives up  '), ('viel', 'a lot  '), ('vielleicht', 'maybe  '), ('visitenkarte', 'business card  '), ('vor', 'before  '), ('vorbei', 'past  '), ('vorbereitung', 'preparation  '), ('vorfall', 'incident  '), ('vorherigen', 'previous  '), ('vorlie', 'available  '), ('vorn', 'front  '), ('vorschlag', 'suggestion  '), ('vorsicht', 'caution  '), ('vorsichtig', 'careful  '), ('vorteil', 'advantage  '), ('vorwort', 'preface  '), ('vorzugten', 'preferred  '), ('vorüber', 'over  '), ('völlig', 'completely  '), ('wach', 'awake  '), ('waffen', 'weapons  '), ('wagen', 'car  '), ('wahr', True), ('war', 'was  '), ('waren', 'were  '), ('warten', 'wait  '), ('was', 'what  '), ('weder', 'neither  '), ('wege', 'ways  '), ('weinen', 'cry  '), ('weit', 'far  '), ('weiter', 'further  '), ('welcher', 'which  '), ('welt', 'world  '), ('wen', 'whom  '), ('wenig', 'few  '), ('wenn', 'if  '), ('wer', 'who  '), ('werde', 'will  '), ('werk', 'Werk  '), ('werte', 'values  '), ('wichtig', 'important  '), ('widerwillig', 'reluctantly  '), ('wieder', 'again  '), ('wiederholt', 'repeatedly  '), ('wiedersehen', 'reunion  '), ('will', 'wants  '), ('willst', 'want  '), ('willybrandtschule', 'Willy Brandt School  '), ('wimper', 'eyelash  '), ('wimpern', 'eyelashes  '), ('wird', 'will  '), ('wirkt', 'acts  '), ('wissen', 'know  '), ('wohnungstür', 'apartment door  '), ('wolken', 'clouds  '), ('wollen', 'want  '), ('wollte', 'wanted  '), ('worden', 'become  '), ('worterklärungen', 'word explanations  '), ('wurden', 'were  '), ('wusste', 'knew  '), ('wussten', 'knew  '), ('während', 'during  '), ('wänden', 'walls  '), ('wäre', 'would be  '), ('wärme', 'warmth  '), ('wünschen', 'wish  '), ('zabee', 'Zabee  '), ('zeibeamter', 'civil servant  '), ('zeigen', 'show  '), ('zeigt', 'shows  '), ('zeitgefühl', 'sense of time  '), ('zeitlupe', 'slow motion  '), ('zeitschriften', 'magazines  '), ('zer', 'produ'), ('zeuge', 'witnesses'), ('zeugnis', 'certificate'), ('ziehen', 'pull'), ('zieht', 'pulls'), ('zierlich', 'delicate'), ('zittern', 'tremble'), ('zitternder', 'trembling'), ('zuerst', 'first'), ('zufall', 'coincidence'), ('zufrieden', 'satisfied'), ('zufriedenheit', 'satisfaction'), ('zufälle', 'coincidences'), ('zugelassenen', 'approved'), ('zuges', 'to'), ('zugänglich', 'accessible'), ('zum', 'to the'), ('zur', 'to the'), ('zurück', 'back'), ('zurückkommen', 'come back'), ('zusammenbleiben', 'stay together'), ('zusammenfassung', 'summary'), ('zusammenprall', 'collision'), ('zusammensein', 'togetherness'), ('zusammensetzt', 'is composed'), ('zweifel', 'doubts'), ('zwischenfall', 'incident'), ('zärtlich', 'tender'), ('ähnlich', 'similar'), ('ändert', 'changes'), ('änderungs', 'change of'), ('öffnet', 'opens'), ('öztürk', 'Öztürk'), ('überfällt', 'attacks'), ('überhaupt', 'at all'), ('übernehmen', 'take over'), ('übernimmt', 'takes over'), ('überprüfen', 'check'), ('überrascht', 'surprised'), ('überreicht', 'handed over'), ('übersicht', 'overview'), ('überwiesen', 'transferred'), ('übrigens', 'by the way'), ('übungen', 'exercises')]

class MatchButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_normal = ""
        self.background_color = (0.94, 0.95, 0.98, 1)
        self.color = (0.12, 0.14, 0.20, 1)
        self.font_size = dp(17)
        self.bold = True

class MatchGame(BoxLayout):
    score = NumericProperty(0)
    streak = NumericProperty(0)
    lives = NumericProperty(3)
    round_no = NumericProperty(1)
    message = StringProperty("Match each German word with its meaning.")

    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", padding=dp(18), spacing=dp(12), **kwargs)
        self.selected_de = None
        self.selected_en = None
        self.locked = False
        self.build_header()
        self.build_board()
        self.new_round()

    def build_header(self):
        top = BoxLayout(size_hint_y=None, height=dp(60), spacing=dp(8))
        title = Label(text="[b]Deutsch Match[/b]", markup=True,
                      font_size=dp(24), color=(0.10,0.12,0.18,1))
        stats = Label(text=self.stats_text(), font_size=dp(14),
                      color=(0.25,0.27,0.32,1), halign="right")
        self.stats_label = stats
        top.add_widget(title)
        top.add_widget(stats)
        self.add_widget(top)

        self.progress = ProgressBar(max=10, value=0, size_hint_y=None, height=dp(8))
        self.add_widget(self.progress)

        msg = Label(text=self.message, font_size=dp(15),
                    color=(0.30,0.32,0.38,1), size_hint_y=None, height=dp(35))
        self.message_label = msg
        self.add_widget(msg)

    def stats_text(self):
        return f"❤️ {self.lives}   ⭐ {self.score}   🔥 {self.streak}"

    def build_board(self):
        self.board = GridLayout(cols=2, spacing=dp(10), padding=(0, dp(8)))
        self.add_widget(self.board)

        restart = Button(text="↻  New Game", size_hint_y=None, height=dp(48),
                         background_normal="", background_color=(0.20,0.55,0.95,1),
                         color=(1,1,1,1), font_size=dp(16), bold=True)
        restart.bind(on_release=lambda *_: self.reset_game())
        self.add_widget(restart)

    def new_round(self):
        if self.lives <= 0:
            return
        self.selected_de = None
        self.selected_en = None
        self.locked = False
        self.message = "Match each German word with its meaning."
        self.message_label.text = self.message
        self.board.clear_widgets()

        pairs = random.sample(WORDS, 5)
        self.current_pairs = pairs

        german = [p[0] for p in pairs]
        english = [p[1] for p in pairs]
        random.shuffle(german)
        random.shuffle(english)

        self.de_buttons = {}
        self.en_buttons = {}

        for word in german:
            b = MatchButton(text=word)
            b.bind(on_release=lambda btn, w=word: self.select_de(w, btn))
            self.de_buttons[word] = b
            self.board.add_widget(b)

        for meaning in english:
            b = MatchButton(text=meaning)
            b.bind(on_release=lambda btn, m=meaning: self.select_en(m, btn))
            self.en_buttons[meaning] = b
            self.board.add_widget(b)

        self.remaining = len(pairs)
        self.progress.value = 0
        self.stats_label.text = self.stats_text()

    def select_de(self, word, button):
        if self.locked or button.disabled:
            return
        self.selected_de = (word, button)
        button.background_color = (0.55, 0.80, 1, 1)
        self.try_match()

    def select_en(self, meaning, button):
        if self.locked or button.disabled:
            return
        self.selected_en = (meaning, button)
        button.background_color = (0.55, 0.80, 1, 1)
        self.try_match()

    def try_match(self):
        if not self.selected_de or not self.selected_en:
            return

        de, de_btn = self.selected_de
        en, en_btn = self.selected_en

        correct = any(a == de and b == en for a, b in self.current_pairs)

        if correct:
            self.locked = True
            de_btn.background_color = (0.45, 0.85, 0.55, 1)
            en_btn.background_color = (0.45, 0.85, 0.55, 1)
            de_btn.disabled = True
            en_btn.disabled = True
            self.score += 10
            self.streak += 1
            self.remaining -= 1
            self.progress.value = 10 - self.remaining
            self.message = "✓ Correct!"
            self.message_label.text = self.message
            self.stats_label.text = self.stats_text()
            self.selected_de = None
            self.selected_en = None
            Clock.schedule_once(self.unlock, 0.25)
            if self.remaining == 0:
                Clock.schedule_once(lambda *_: self.next_round(), 0.45)
        else:
            self.lives -= 1
            self.streak = 0
            self.message = "✗ Not a match — try again."
            self.message_label.text = self.message
            self.stats_label.text = self.stats_text()
            de_btn.background_color = (1, 0.55, 0.55, 1)
            en_btn.background_color = (1, 0.55, 0.55, 1)
            self.locked = True
            Clock.schedule_once(lambda *_: self.reset_selection(de_btn, en_btn), 0.45)
            if self.lives <= 0:
                Clock.schedule_once(lambda *_: self.game_over(), 0.5)

    def unlock(self, *_):
        self.locked = False

    def reset_selection(self, de_btn, en_btn):
        de_btn.background_color = (0.94, 0.95, 0.98, 1)
        en_btn.background_color = (0.94, 0.95, 0.98, 1)
        self.selected_de = None
        self.selected_en = None
        self.locked = False

    def next_round(self):
        self.round_no += 1
        self.new_round()

    def game_over(self):
        self.board.clear_widgets()
        self.message = f"Game over! Final score: {self.score}"
        self.message_label.text = self.message
        self.progress.value = 10

    def reset_game(self):
        self.score = 0
        self.streak = 0
        self.lives = 3
        self.round_no = 1
        self.new_round()

class GermanMatchApp(App):
    title = "Deutsch Match"

    def build(self):
        return MatchGame()

if __name__ == "__main__":
    GermanMatchApp().run()
