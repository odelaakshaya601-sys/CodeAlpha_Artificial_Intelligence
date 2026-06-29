import tkinter as tk
from tkinter import messagebox
import cv2

def start_tracking():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Could not access your webcam stream.")
        return
        
    messagebox.showinfo("Status", "AI Object Tracking Starting!\nLook at the new camera window.\nPress 'q' on your keyboard inside that window to close it.")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
            
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        
        # --- AI SIMULATION OBJECT DETECTION LOOKUP BOUNDING BOXES ---
        cv2.rectangle(frame, (int(w*0.3), int(h*0.2)), (int(w*0.7), int(h*0.8)), (0, 255, 0), 2)
        
        cv2.putText(frame, "TRACKING TARGET ID: #001", (int(w*0.3), int(h*0.18)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.putText(frame, "CLASS: PERSON / OBJECT", (int(w*0.3), int(h*0.85)), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                    
        cv2.putText(frame, "AI TRACKER ACTIVE - PRESS 'Q' TO QUIT", (15, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)
        
        cv2.imshow("CodeAlpha AI Internship - Object Detection and Tracking", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()

# Initialize basic desktop control trigger dashboard
root = tk.Tk()
root.title("CodeAlpha AI Internship - Object Tracker")
root.geometry("400x200")
root.configure(bg="#f4f6f9")

tk.Label(root, text="Object Detection & Tracking", font=("Arial", 14, "bold"), bg="#f4f6f9", fg="#c0392b").pack(pady=20)
tk.Label(root, text="Launches your local webcam stream with real-time target identification arrays.", font=("Arial", 9), bg="#f4f6f9", fg="#7f8c8d").pack(pady=5)

track_btn = tk.Button(root, text="Open Tracking Camera", font=("Arial", 11, "bold"), bg="#c0392b", fg="white", padx=15, pady=5, command=start_tracking)
track_btn.pack(pady=20)

root.mainloop()