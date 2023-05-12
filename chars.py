import matplotlib.pyplot as mpl

def generate_bar_chart(labels, values):
    fig, ax = mpl.subplots()
    ax.bar(labels, values)

    ax.set_title('My Bar Chart')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    mpl.show()

def generate_pie_chart(labels, values):
    fig, ax = mpl.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    mpl.show()

if __name__ == '__main__':
    labels = ['A', 'B', 'C']
    values = [100, 40, 200]
    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)