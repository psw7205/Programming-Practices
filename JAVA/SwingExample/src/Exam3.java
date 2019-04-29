import java.awt.Color;
import java.awt.Graphics;
import java.awt.Point;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;
import java.util.ArrayList;

import javax.swing.ButtonGroup;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JRadioButtonMenuItem;
import javax.swing.SwingUtilities;

class Rect3 {
	Point p1 = new Point();
	Point p2 = new Point();
	Color color;

	void draw(Graphics g) {
		int x = p1.x;
		int y = p1.y;
		int w = p2.x - p1.x;
		if (w < 0) {
			x = p2.x;
			w = -w;
		}
		
		int h = p2.y - p1.y;
		if (h < 0) {
			y = p2.y;
			h = -h;
		}
		g.setColor(color);
		g.fillRect(x, y, w, h);
		g.setColor(Color.BLACK);
		g.drawRect(x, y, w, h);
	}
}

class P3 extends JPanel implements MouseListener, MouseMotionListener {
	Color color = Color.RED;
	Point p1, p2;
	ArrayList<Rect3> ar = new ArrayList<>();
	JLabel l = new JLabel();
	
	P3() {
		this.addMouseListener(this);
		this.addMouseMotionListener(this);
		add(l);
	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);
		
		for(Rect3 r : ar)
			r.draw(g);

		l.setText(""+ar.size());
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {
		
		if(SwingUtilities.isLeftMouseButton(arg0))
			ar.get(ar.size() - 1).p2 = arg0.getPoint();
		
		repaint();
	}

	@Override
	public void mouseMoved(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseClicked(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent arg0) {
		if(SwingUtilities.isLeftMouseButton(arg0))
		{
			Rect3 tmp = new Rect3();
			tmp.p1 = arg0.getPoint();
			
			tmp.p2.x = arg0.getX();
			tmp.p2.y = arg0.getY();
			tmp.color = color;
			
			ar.add(tmp);
		}
		
		
		repaint();
	}

	@Override
	public void mouseReleased(MouseEvent arg0) {
		if(SwingUtilities.isLeftMouseButton(arg0))
			ar.get(ar.size() - 1).p2 = arg0.getPoint();

		
		repaint();
	}
}

class F3 extends JFrame implements ActionListener {

	JRadioButton i1, i2, i3;
	P3 p;

	F3() {
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JMenuBar bar = new JMenuBar();
		JMenu menu = new JMenu("Color");
		ButtonGroup group = new ButtonGroup();

		bar.add(menu);

		i1 = new JRadioButton("red");
		i1.addActionListener(this);
		i1.setSelected(true);

		i2 = new JRadioButton("green");
		i2.addActionListener(this);

		i3 = new JRadioButton("blue");
		i3.addActionListener(this);

		group.add(i1);
		group.add(i2);
		group.add(i3);

		menu.add(i1);
		menu.add(i2);
		menu.add(i3);

		p = new P3();
		add(p);

		this.setJMenuBar(bar);
		this.setVisible(true);
	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		if (arg0.getSource() == i1)
			p.color = Color.RED;
		else if (arg0.getSource() == i2)
			p.color = Color.GREEN;
		else if (arg0.getSource() == i3)
			p.color = Color.BLUE;
	}

}

public class Exam3 {

	public static void main(String[] args) {
		new F3();
	}

}
