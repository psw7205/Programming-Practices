import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Iterator;
import java.util.LinkedList;

import javax.swing.BorderFactory;
import javax.swing.DefaultListModel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JList;
import javax.swing.JPanel;
import javax.swing.ListSelectionModel;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;

class R5 extends JPanel {
	LinkedList<Point> pointList = new LinkedList<>();
	L5 l;
	int selected = -1;

	R5() {
		this.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent arg0) {
				pointList.add(arg0.getPoint());
				l.updateList();
				repaint();
			}
			
		});

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		int i = 0;
		for (Point p : pointList) {
			int r = 50;

			if (i == selected)
				g.setColor(Color.red);
			else
				g.setColor(Color.black);

			g.drawOval(p.x - r, p.y - r, 2 * r, 2 * r);
			i++;
		}
	}

	void removeSelected() {
		
		if (selected < 0)
			return;
		
		Iterator<Point> it = pointList.iterator();
		int i = 0;
		for (; it.hasNext();) {
			it.next();
			if (i == selected) {
				it.remove();
				break;
			}
			i++;
		}
		selected = -1;
	}
}

class L5 extends JPanel implements ListSelectionListener {
	R5 r;
	JList list;
	DefaultListModel listModel;
	JButton btn;

	L5() {
		this.setBackground(Color.GRAY);
		listModel = new DefaultListModel();
		list = new JList(listModel);

		list.setBorder(BorderFactory.createLineBorder(Color.black, 1));
		list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
		list.addListSelectionListener(this);
		list.setPreferredSize(new Dimension(200, 400));
		
		add(list);
		
		btn = new JButton("Delete");
		btn.addActionListener(new ActionListener()
		{
			@Override
			public void actionPerformed(ActionEvent e) {
				r.removeSelected();
				updateList();				
			}
	
		});
		add(btn);
	}

	@Override
	public void valueChanged(ListSelectionEvent e) {
		int index = list.getSelectedIndex();
		r.selected = index;
		r.repaint();

	}

	void updateList() {
		listModel.clear();

		int i = 0;
		for (Point p : r.pointList) {
			String str = new String();
			str = i + ": center(" + p.x + "," + p.y + ")";
			listModel.addElement(str);
			i++;
		}
	}
	
}

public class Exam5 extends JFrame {

	Exam5() {
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		R5 r = new R5();
		L5 l = new L5();
		l.setPreferredSize(new Dimension(200,500));
		
		this.add(r, BorderLayout.CENTER);
		this.add(l, BorderLayout.WEST);
		
		r.l = l;
		l.r = r;
		
		this.setVisible(true);
	}

	public static void main(String[] args) {
		new Exam5();
	}

}
