import datetime
import os
import sys

class logger:
    def __init__(self):
        try:
            # Create logs directory if it doesn't exist
            current_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
            parent_dir = os.path.dirname(current_dir)
            logs_dir = os.path.join(parent_dir, 'logs')

            if not os.path.exists(logs_dir):
                os.makedirs(logs_dir)
        except:
            print("Error creating logs directory")
            sys.exit(1)

        try:
            # Create log file
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            self.log_file = os.path.join(logs_dir, f'log_{timestamp}.txt')
            open(self.log_file, 'w')
            
            # Log the start of the program
            self.log('Logging started')
        except:
            print("Error creating log file")
            sys.exit(1)
        
    def log(self, message):
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_message = f'{timestamp} - {message}'
        with open(self.log_file, 'a') as f:
            f.write(log_message + '\n')

    def close(self):
        self.log('Logging ended')