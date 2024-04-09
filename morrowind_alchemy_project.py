
#importing libraries
import pyfiglet as pfig

#Dictionary of all ingredients and their effects
ingredients = {'alit hide': ['drain intelligence', 'resist poison', 'telekinesis','detect animal'],
'ampoule pod': ['water walking', 'paralyze','detect animal', 'drain willpower'],
'ash salts': ['drain agility', 'resist magicka', 'cure blight disease' 'resist magicka'],
'ash yam': ['fortify intelligence', 'fortify strength', 'resist common disease', 'detect key'],
'bittergreen petal': ['restore intelligence', 'invisibility', 'drain endurance', 'drain magicka'],
'black anther': ['drain agility', 'resist fire', 'drain endurance', 'light'],
'black lichen': ['drain strength', 'resist frost', 'drain speed', 'cure poison'],
'bloat': ['drain magicka','fortify intelligence','fortify willpower','detect animal'],
'bonemeal': ['restore agility', 'telekinesis', 'drain fatigue', 'drain personality'],
'bread': ['restore fatigue'],
"bungler's bane": ['drain speed', 'drain endurance', 'dispel', 'drain strength'],
'chokeweed': ['drain luck', 'restore fatigue', 'cure common disease', 'drain willpower'],
'coda flower': ['drain personality', 'levitate', 'drain intelligence', 'drain health'],
'comberry': ['drain fatigue', 'restore magicka', 'fire shield', 'reflect'],
'corkbulb root': ['cure paralyzation', 'restore health', 'lightning shield', 'fortify luck'],
'corprus weepings': ['drain fatigue', 'fortify luck', 'drain willpower', 'restore health'],
'crab meat': ['restore fatigue','resist shock','lightning shield','restore luck'],
'daedra skin': ['fortify strength','cure common disease','paralyze','swift swim'],
"daedra's heart": ['restore magicka','fortify endurance','drain agility','night eye'],
'diamond': ['drain agility','invisibility','reflect','detect key'],
'dreugh wax': ['fortify strength','restore strength','drain luck','drain willpower'],
'ectoplasm': ['fortify agility','detect animal','drain strength','drain health'],
'emerald': ['fortify magicka','restore health','drain agility','drain endurance'],
'fire petal': ['resist fire','drain health','spell absorption','paralyze'],
'fire salts': ['drain health','fortify agility','resist frost','fire shield'],
'frost salts': ['drain speed','restore magicka','frost shield','resist fire'],
'ghoul heart': ['paralyze','cure poison','fortify attack'],
'gold kanet': ['drain health','burden','drain luck','restore strength'],
'gravedust': ['drain intelligence','cure common disease','drain magicka','restore endurance'],
'green lichen': ['fortify personality','cure common disease','drain strength','drain health'],
'guar hide': ['drain fatigue','fortify endurance','restore personality','fortify luck'],
'hackle-lo leaf': ['restore fatigue','paralyze','water breathing','restore luck'],
'heather': ['restore personality','feather','drain speed','drain personality'],
'hound meat': ['restore fatigue','fortify fatigue','reflect','detect enchantment'],
'hypha facia': ['drain luck','drain agility','drain fatigue','detect enchantment'],
'kagouti hide': ['drain fatigue','fortify speed','resist common disease','night eye'],
'kresh fiber': ['restore luck', 'fortify personality', 'drain magicka', 'drain speed'],
'kwama cuttle': ['resist poison','drain fatigue','water walking','water breathing'],
'large kwama egg': ['restore fatigue','paralyze','frost shield','fortify health'],
'luminous russula': ['water breathing','drain fatigue','poison'],
'marshmerrow': ['restore health','detect enchantment','drain willpower','drain fatigue'],
'moon sugar': ['fortify speed','dispel','drain endurance','drain luck'],
'muck': ['drain intelligence','detect key','drain personality','cure common disease'],
'netch leather': ['fortify endurance','fortify intelligence','drain personality','cure paralyzation'],
'pearl': ['drain agility','dispel','water breathing','resist common disease'],
'racer plumes': ['drain willpower','levitate'],
'rat meat': ['drain magicka','paralyze','cure poison','resist poison'],
'raw ebony': ['drain agility','cure poison','frost shield','restore speed'],
'raw glass': ['drain intelligence','drain strength','drain speed','fire shield'],
'red lichen': ['drain speed','light','cure common disease','drain magicka'],
'resin': ['restore health','restore speed','burden','resist common disease'],
'roobrush': ['drain willpower','fortify agility','drain health','cure poison'],
'ruby': ['drain health','feather','restore intelligence','drain agility'],
'saltrice': ['restore fatigue','fortify magicka','drain strength','restore health'],
'scales': ['drain personality','water walking','restore endurance','swift swim'],
'scamp skin': ['drain magicka','cure paralyzation','restore personality','restore strength'],
'scathecraw': ['drain strength','cure poison','drain health','restore willpower'],
'scrap metal': ['drain health','lightning shield','resist shock','restore intelligence'],
'scrib jelly': ['fortify willpower','cure poison','cure blight disease','restore willpower'],
'scrib jerky': ['restore fatigue','fortify fatigue','burden','swift swim'],
'scuttle': ['restore fatigue','fortify fatigue','feather','telekinesis'],
'shalk resin': ['drain fatigue','fortify health','drain personality','fortify speed'],
'sload soap': ['drain personality','fortify agility','fire shield','restore agility'],
'small kwama egg': ['restore fatigue'],
'spore pod': ['drain strength','drain fatigue','detect key','paralyze'],
'stoneflower petals': ['restore strength','fortify magicka','drain luck','fortify personality'],
'trama root': ['restore willpower','levitate','drain magicka','drain speed'],
'vampire dust': ['fortify health','fortify strength','spell absorption','vampirism'],
'violet coprinus': ['water walking','drain fatigue','poison'],
'void salts': ['restore magicka','spell absorption','paralyze','drain endurance'],
'wickwheat': ['restore health','fortify willpower','paralyze','damage intelligence'],
'willow anther': ['drain personality','frost shield','cure common disease','cure paralyzation']
}

#list of effects used for iteration in fucntion
listOfEffects = ['blind','burden','night eye','cure blight disease','cure common disease','paralyze','cure paralyzation','cure poison','poison','damage fatigue','damage health','drain speed','resist common disease',
                'damage intelligence','damage magicka','detect animal','drain strength','detect enchantment','resist frost','detect key','dispel','resist magicka','drain alteration','drain agility','feather','fire shield',
                'restore agility','drain endurance','restore endurance','restore fatigue','drain fatigue','fortify attack','fortify endurance','fortify fatigue','restore health','fortify health','fortify intelligence',
                'fortify luck','fortify magicka','restore luck','drain health','fortify maximum magicka','fortify personality','fortify speed','restore personality','restore speed','fortify strength','restore strength',
                'drain intelligence','restore willpower','fortify willpower','spell absorption','drain luck','frost shield','telekinesis','invisibility','vampirism','water breathing','levitate','water walking','light',
                'weakness to fire','weakness to poison','drain magicka','drain personality','recall','reflect','resist fire','drain willpower','resist paralysis','resist poison','resist shock','fortify agility',
                'restore intelligence','restore magicka','frost damage','swift swim','lightning shield']

#search engine function, takes 1 parameter 'choice' which is given as an input in the program. The function will preform an elif loop based on choice passed in
def searchEngine(choice):
    while True:
        #choice 1 will ask for an ingredient and then convert it to lower case to check it in dictionary and return all efects of that ingredient
        if choice == 1:
            ingredient = input('Enter ingredient name: ').lower()
            if ingredient in ingredients:
                return ingredients[ingredient]
            else:
                print('Ingredient not found. Please try again.')
        #choice 2 will ask for an effect as input and then convert that to lower case which it will then check to see if it matches an effect in the list of effects. 
        #If it does it will iterate through the dictionary checking for all instances of that effect and the retrun all ingredients with that effect. 
        elif choice == 2:
            effect = input('Enter effect name: ').lower()
            if effect in listOfEffects:
                foundKeys = []
                for key, value in ingredients.items():
                    if effect in value:
                        foundKeys.append(key)
                return foundKeys
            else:
                print('Effect not found. Please try again.') 
        else:
            print('Invalid choice. Please choose again.')
            # If choice is invalid, ask the user for input again
            print('1. list effects of ingredient')
            print('2. search for ingredient by effect')
            choice = int(input('Please select an option'))

#this function is a loop that will ask the user which choice they want to make and will repeat over and over again until the user selects the exit option
def programLoop():
    while True:
        print('1. List effects of ingredient')
        print('2. Search for ingredient by effect')
        print('3. Exit')
        choice = int(input('Please select an option: '))
        
        if choice == 1 or choice == 2:
            searchEngine(choice)
        elif choice == 3:
            print('Exiting the program...')
            break  # Exit the loop
        else:
            print('Invalid choice. Please select again.')


#printing intro graphic
print(pfig.figlet_format("Morrowind Alchemy Project V1.0", font="Big",justify='center',width=100))

programLoop()