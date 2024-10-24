import json

class Decoder():
    def main():
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','å','ä','ö']
        encodedAlphabet = ['z','x','c','v','n','b','m','g','d','f','s','a','l','j','h','k','ä','ö','w','q','e','r','y','t','u','i','å','p','o']
        running = True
        while running:
            def encode():
                print('Syötä salattava viesti')
                message = input()
                encodedMessage = ''
                for char in message:
                    if char.lower() in alphabet:
                        if char.isupper():
                            encodedMessage =  encodedMessage + char.replace(char, encodedAlphabet[alphabet.index(char.lower())].upper())
                        else:
                            encodedMessage =  encodedMessage + char.replace(char, encodedAlphabet[alphabet.index(char)])
                    else:
                        encodedMessage =  encodedMessage + char
                        
                print(encodedMessage)

                print('Haluatko tallentaa viestin? "Kyllä" tai "Ei"')
                save = input()

                if save == 'Kyllä':
                    print('Anna viestille nimi')
                    title = input()
                    messageData = {
                        'title': title,
                        'message': encodedMessage
                    }
                    with open('messages.json', 'r+') as file:
                        fileData = json.load(file)
                        fileData['messages'].append(messageData)
                        file.seek(0)
                        json.dump(fileData, file, indent = 4)


            def decode(message):
                decodedMessage = ''
                for char in message:
                    if char.lower() in encodedAlphabet:
                        if char.isupper():
                            decodedMessage =  decodedMessage + char.replace(char, alphabet[encodedAlphabet.index(char.lower())]).upper()
                        else:
                            decodedMessage =  decodedMessage + char.replace(char, alphabet[encodedAlphabet.index(char)])
                    else:
                        decodedMessage =  decodedMessage + char
                return decodedMessage

            def load():
                with open('messages.json', 'r') as file:
                    data = json.load(file)
                    for message in data['messages']:
                        print('nimi:' + message['title'])
                    
                    print('Syötä ladattavan viestin nimi')
                    messageToLoad = input()
                    with open('messages.json', 'r+') as file:
                        fileData = json.load(file)
                        for message in fileData['messages']:
                            if message['title'] == messageToLoad:
                                print(message['message'])
                                decodedMessage = decode(message['message'])
                                print('Salattu: ' + message['message'] + '\n' + 'Purettu: ' + decodedMessage)

            def delete():
                with open('messages.json', 'r') as file:
                    data = json.load(file)
                    for message in data['messages']:
                        print('nimi: ' + message['title'])
                    
                    print('Syötä poistettavan viestin nimi')
                    messageToLoad = input()
                    with open('messages.json', 'r+') as file:
                        fileData = json.load(file)
                        i = 0
                        for message in fileData['messages']:
                            if message['title'] == messageToLoad:
                                fileData['messages'].pop(i)
                                with open('messages.json', 'w') as file:
                                    json.dump(fileData, file, indent = 4)
                            else:
                                i = i+1


            welcome = ['Tervetuloa salaviesti appiin!',
                        'Syötä toiminto:', '"Salaa viesti" salataksesi viestin',
                        '"Pura viesti" purkaaksesi viestin salaus', '"Lataa viesti" ladataksesi tallennetun viestin',
                        '"Poista viesti poistaaksesi tallennetun viestin',
                        '"Sulje" sulkeaksesi ohjelman']
            
            for line in welcome:
                print(line, sep='\n')

            action = input()

            if action == 'Salaa viesti':
                encode()
            if action == 'Pura viesti':
                print('Syötä salattu viesti purkaaksesi se')
                message = input()
                decodedMessage = decode(message)
                print(decodedMessage)
            if action == 'Sulje':
                running = False
            if action == 'Lataa viesti':
                load()
            if action == 'Poista viesti':
                delete()

    main()