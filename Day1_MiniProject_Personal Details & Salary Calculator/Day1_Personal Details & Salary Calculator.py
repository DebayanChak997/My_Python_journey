import tkinter as tk


def detailscalc():
    ffname=fnameentry.get();
    llname=lnameentry.get();
    agee=int(ageentry.get());
    salary=float(mnthlysalarye.get());
    
    yesrlysalary= salary*12
    Future_Age=agee+5
    
    Details.config(
        text=f"FirstName: {ffname} LastName: {llname} \nAge after 5 years: {Future_Age}\nYearly Salary: ₹{yesrlysalary}"
)



root = tk.Tk()
root.title("Test")
root.geometry("300x300")
tk.Label(root, text="Tkinter Works")


fname=tk.Label(root, text="First Name")
fnameentry=tk.Entry(root)

lname=tk.Label(root, text="Last Name")
lnameentry=tk.Entry(root)

age=tk.Label(root, text="Age")
ageentry=tk.Entry(root)

mnthlysalary=tk.Label(root, text="Monthly Salary")
mnthlysalarye=tk.Entry(root)

calc_btn=tk.Button(root,text = 'Calculate', command= detailscalc)

Details=tk.Label(root,text="")


fname.grid(row=0,column=0)
fnameentry.grid(row=0,column=1)
lname.grid(row=1,column=0)
lnameentry.grid(row=1,column=1)
age.grid(row=2,column=0)
ageentry.grid(row=2,column=1)
mnthlysalary.grid(row=3,column=0)
mnthlysalarye.grid(row=3,column=1)
calc_btn.grid(row=4,column=1)

Details.grid(row=6,column=0)
root.mainloop()