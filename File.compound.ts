document.addEventListener('DOMContentLoaded', function() {
    const pdfInput: HTMLInputElement = document.getElementById('pdfInput') as HTMLInputElement;
    const chatContainer: HTMLElement = document.getElementById('chatContainer') as HTMLElement;
    const userInput: HTMLInputElement = document.getElementById('userInput') as HTMLInputElement;
    const sendButton: HTMLButtonElement = document.getElementById('sendButton') as HTMLButtonElement;
  
    pdfInput.addEventListener('change', handleFileUpload);
  
    sendButton.addEventListener('click', sendMessage);
  
    function handleFileUpload(event: Event) {
      const target = event.target as HTMLInputElement;
      const file: File | null = target.files ? target.files[0] : null;
      if (file) {
       
        appendMessage('Uploaded PDF: ' + file.name);
      }
    }
  
    function sendMessage() {
      const message: string = userInput.value.trim();
      if (message) {
       
        appendMessage('You: ' + message);
        userInput.value = ''; // Clear the input field
      }
    }
  
    function appendMessage(message: string) {
      const messageElement: HTMLDivElement = document.createElement('div');
      messageElement.textContent = message;
      chatContainer.appendChild(messageElement);
      chatContainer.scrollTop = chatContainer.scrollHeight;
    }
  });
  