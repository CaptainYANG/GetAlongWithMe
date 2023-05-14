
# Text guidance.
# This is written to maintain a good relationship between us.
# You can open an issue to file a bug.
# Updated 2023/05/14.

def feelings_input():
    while True:
        have_feelings = input(f'Do you think I have feelings for you? Y or N.').upper()
        if have_feelings in ['Y', 'N']:
            return True if have_feelings == 'Y' else False
        else:
            print('Please type Y or N.')
            continue
        
def reply_sla_input():
    while True:
        response_required = input('Check my last message, do you think I expect a reply? Y or N').upper()
        if response_required in ['Y', 'N']:
            if response_required == 'Y':
                return quick_reply_required()
            else:
                return 24
        else:
            print('Please type Y or N.')
            continue

def quick_reply_required():
    while True:
        quick_reply_required = input('Do you think this is a text message that requires quick reply? Y or N').upper()
        if quick_reply_required in ['Y', 'N']:
            return 1 if quick_reply_required == 'Y' else 3
        else:
            print('Please type Y or N.')
            continue
def text_response_time_input():
    while True:
        try:
            response_hours = int(input('You reply to my messages after how many hours? Type a number.'))
            return response_hours
        except Exception:
            print('Please type a number')
            continue
        
def take_actions(reply_sla, response_hours):
    if response_hours > reply_sla:
        print('Appologize and explain : ) .')
    else:
        print('You are the best > 3 <')
        pass

print(f'Welcome! Please answer the questions below using your common sense and follow my rules.')
have_feelings = feelings_input()
if not have_feelings:
    print("Do whatever you want. We are good.")
    quit()
reply_sla = reply_sla_input()
response_hours = text_response_time_input()
take_actions(reply_sla, response_hours)
