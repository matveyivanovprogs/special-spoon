sent_message = 'Hey there! This is a secret message.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)
with open('sent_message.txt', 'r+') as file:
  # Read the sent message from the file
  original_message = file.read()  
  # Move the cursor to the beginning of the file
  file.seek(0)
  # Modify the message to simulate unsending
  unsent_message = 'This message has been unsent.'
    # Truncate the file to the size of the unsent message
  file.truncate(len(unsent_message))
  #Write the modified message in place of the old message
  file.write(unsent_message)

# Display the modified message
print('Original Message:', original_message)
print('Unsent Message:', unsent_message)

