"""
Main entry point for TPAO Bot
Improved version with better structure and error handling
"""
import sys
import tkinter as tk
from tkinter import messagebox
from config import CONFIG_FILE, VERSION, WINDOW_WIDTH, WINDOW_HEIGHT
from validators import ValidationError
from bot_engine import start_bot
from config import BotConfig


class MainWindow:
    """Main application window"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Setup window properties"""
        self.root.title(f"TPAO Bot - {VERSION}")
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
        self.center_window()
        self.root.resizable(False, False)
    
    def center_window(self):
        """Center window on screen"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (WINDOW_WIDTH // 2)
        y = (self.root.winfo_screenheight() // 2) - (WINDOW_HEIGHT // 2)
        self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{x}+{y}")
    
    def create_widgets(self):
        """Create and place UI widgets"""
        # Title
        title_label = tk.Label(
            self.root, 
            text="TPAO Bot", 
            font=("Arial Bold", 25),
            anchor='center'
        )
        title_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Configure button
        config_button = tk.Button(
            self.root,
            text="Configurar",
            width=20,
            command=self.open_config_window
        )
        config_button.place(relx=0.5, rely=0.4, anchor="center")
        
        # Start button
        start_button = tk.Button(
            self.root,
            text="Iniciar",
            width=20,
            command=self.start_bot
        )
        start_button.place(relx=0.5, rely=0.7, anchor="center")
        
        # Version label
        version_label = tk.Label(
            self.root,
            text=f"v{VERSION}",
            font=("Arial Bold", 10),
            anchor='center'
        )
        version_label.place(relx=0.7, rely=0.9, anchor="center")
    
    def open_config_window(self):
        """Open configuration window"""
        self.root.withdraw()  # Hide main window
        config_window = ConfigWindow(self.root)
        config_window.show()
    
    def start_bot(self):
        """Start the bot with saved configuration"""
        try:
            config = BotConfig.from_file(CONFIG_FILE)
            self.root.destroy()
            start_bot(config.meditation_key, config.click_position)
        except FileNotFoundError:
            messagebox.showerror(
                "Error", 
                "Archivo de configuración no encontrado. Por favor configure el bot primero."
            )
        except Exception as e:
            messagebox.showerror("Error", f"Error al iniciar el bot: {e}")
    
    def run(self):
        """Start the main application"""
        self.root.mainloop()


class ConfigWindow:
    """Configuration window"""
    
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel()
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Setup configuration window"""
        self.window.title("Configuración del Bot")
        self.window.geometry("400x300")
        self.center_window()
        self.window.resizable(False, False)
        
        # Handle window close
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)
    
    def center_window(self):
        """Center window on screen"""
        self.window.update_idletasks()
        x = (self.window.winfo_screenwidth() // 2) - 200
        y = (self.window.winfo_screenheight() // 2) - 150
        self.window.geometry(f"400x300+{x}+{y}")
    
    def create_widgets(self):
        """Create configuration form widgets"""
        # Title
        title_label = tk.Label(
            self.window,
            text="Configuración del Bot",
            font=("Arial Bold", 18),
            anchor='center'
        )
        title_label.place(relx=0.5, rely=0.1, anchor="center")
        
        # Meditation key
        tk.Label(
            self.window,
            text="Tecla de Meditar:",
            font=("Arial Bold", 12)
        ).place(relx=0.2, rely=0.3, anchor="center")
        
        self.meditation_key_var = tk.StringVar()
        meditation_entry = tk.Entry(
            self.window,
            textvariable=self.meditation_key_var,
            width=15
        )
        meditation_entry.place(relx=0.7, rely=0.3, anchor="center")
        
        # X Position
        tk.Label(
            self.window,
            text="Posición X:",
            font=("Arial Bold", 12)
        ).place(relx=0.2, rely=0.5, anchor="center")
        
        self.pos_x_var = tk.StringVar()
        pos_x_entry = tk.Entry(
            self.window,
            textvariable=self.pos_x_var,
            width=15
        )
        pos_x_entry.place(relx=0.7, rely=0.5, anchor="center")
        
        # Y Position
        tk.Label(
            self.window,
            text="Posición Y:",
            font=("Arial Bold", 12)
        ).place(relx=0.2, rely=0.7, anchor="center")
        
        self.pos_y_var = tk.StringVar()
        pos_y_entry = tk.Entry(
            self.window,
            textvariable=self.pos_y_var,
            width=15
        )
        pos_y_entry.place(relx=0.7, rely=0.7, anchor="center")
        
        # Save button
        save_button = tk.Button(
            self.window,
            text="Guardar y Iniciar",
            width=15,
            command=self.save_and_start
        )
        save_button.place(relx=0.5, rely=0.9, anchor="center")
    
    def save_and_start(self):
        """Save configuration and start bot"""
        try:
            from validators import validate_and_show_errors
            
            # Validate inputs
            meditation_key, pos_x, pos_y = validate_and_show_errors(
                self.meditation_key_var.get(),
                self.pos_x_var.get(),
                self.pos_y_var.get()
            )
            
            # Create and save config
            config = BotConfig(meditation_key, (pos_x, pos_y))
            config.save_to_file(CONFIG_FILE)
            
            # Close windows and start bot
            self.window.destroy()
            self.parent.destroy()
            start_bot(meditation_key, (pos_x, pos_y))
            
        except ValidationError:
            # Error already shown by validator
            pass
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar configuración: {e}")
    
    def on_close(self):
        """Handle window close"""
        self.window.destroy()
        self.parent.deiconify()  # Show main window again
    
    def show(self):
        """Show the configuration window"""
        self.window.mainloop()


def main():
    """Main entry point"""
    try:
        app = MainWindow()
        app.run()
    except Exception as e:
        messagebox.showerror("Error Fatal", f"Error al iniciar la aplicación: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
