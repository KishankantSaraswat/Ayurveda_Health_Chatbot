import tkinter as tk
from tkinter import ttk

class UserProfile:
    def __init__(self, username, health_goals, achievements, points):
        self.username = username
        self.health_goals = health_goals
        self.achievements = achievements
        self.points = points

class GamificationChatbot:
    def __init__(self, root):
        self.root = root
        self.root.title("Gamification Chatbot")

        # Initialize user profile
        self.user_profile = UserProfile("User123", "Lose Weight", [], 100)

        # Create UI elements
        self.create_profile_section()
        self.create_points_section()
        self.create_rewards_section()
        self.create_chat_section()

    def create_profile_section(self):
        profile_frame = ttk.Frame(self.root)
        profile_frame.pack(padx=10, pady=10, anchor="w")

        profile_label = ttk.Label(profile_frame, text="User Profile")
        profile_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        username_label = ttk.Label(profile_frame, text=f"Username: {self.user_profile.username}")
        username_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        goals_label = ttk.Label(profile_frame, text=f"Health Goals: {self.user_profile.health_goals}")
        goals_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    def create_points_section(self):
        points_frame = ttk.Frame(self.root)
        points_frame.pack(padx=10, pady=10, anchor="w")

        points_label = ttk.Label(points_frame, text=f"Points Earned: {self.user_profile.points}")
        points_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    def create_rewards_section(self):
        rewards_frame = ttk.Frame(self.root)
        rewards_frame.pack(padx=10, pady=10, anchor="w")

        rewards_label = ttk.Label(rewards_frame, text="Rewards and Badges")
        rewards_label.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Simulated badges
        badges = ["Badge 1", "Badge 2", "Badge 3"]
        for i, badge in enumerate(badges):
            badge_label = ttk.Label(rewards_frame, text=f"Badge {i + 1}: {badge}")
            badge_label.grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

    def create_chat_section(self):
        chat_frame = ttk.Frame(self.root)
        chat_frame.pack(padx=10, pady=10, anchor="w")

        chat_label = ttk.Label(chat_frame, text="Chat Section")
        chat_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        # Simulated chat messages
        chat_history = ttk.Label(chat_frame, text="Simulated Chat History")
        chat_history.grid(row=1, column=0, padx=10, pady=5, sticky="w")

if __name__ == "__main__":
    root = tk.Tk()
    chatbot = GamificationChatbot(root)
    root.mainloop()
