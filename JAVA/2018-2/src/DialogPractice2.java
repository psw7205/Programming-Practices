import java.awt.FlowLayout;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseMotionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

class CircleInfoDialog extends JDialog {

	JLabel label;
	CircleData data;

	CircleInfoDialog(JFrame frame, String title, boolean modal) {
		super(frame, title, modal);
		label = new JLabel();
		add(label);
		this.setSize(200, 100);
		this.setVisible(true);
	}

	void updateLabel() {
		label.setText("(" + data.x + "," + data.y + ") r = " + data.r);
	}
}

class DialogPanel2 extends JPanel implements ActionListener, MouseListener, MouseMotionListener {
	DialogPractice2 frame;
	CircleData data;

	DialogPanel2() {
		this.addMouseListener(this);
		this.addMouseMotionListener(this);
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {

	}

	@Override
	protected void paintComponent(Graphics g) {
		super.paintComponent(g);

		int x = data.x;
		int y = data.y;
		int r = data.r;

		g.drawOval(x - r, y - r, 2 * r, 2 * r);
	}

	@Override
	public void mouseDragged(MouseEvent arg0) {

		data.r = (data.x - arg0.getX()) * (data.x - arg0.getX()) + (data.y - arg0.getY()) * (data.y - arg0.getY());
		data.r = (int) Math.sqrt((double) data.r);
		frame.setData(data.x, data.y, data.r);
	}

	@Override
	public void mouseMoved(MouseEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub

	}

	@Override
	public void mousePressed(MouseEvent e) {
		data.x = e.getX();
		data.y = e.getY();
		frame.setData(data.x, data.y, 0);
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		data.r = (data.x - e.getX()) * (data.x - e.getX()) + (data.y - e.getY()) * (data.y - e.getY());
		data.r = (int) Math.sqrt((double) data.r);
		frame.setData(data.x, data.y, data.r);
	}
}

class CircleData {
	int x, y, r;
}

public class DialogPractice2 extends JFrame {
	CircleInfoDialog dlg;
	CircleData data;

	DialogPractice2() {
		data = new CircleData();

		this.setSize(300, 300);
		this.setTitle("Dialog Practice");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);

		DialogPanel2 p = new DialogPanel2();
		p.frame = this;
		p.data = data;
		this.add(p);

		dlg = new CircleInfoDialog(this, "모달리스", false);
		dlg.data = data;

		this.setVisible(true);
	}

	void setData(int x, int y, int r) {
		data.x = x;
		data.y = y;
		data.r = r;
		repaint();
		dlg.updateLabel();
	}

	public static void main(String[] args) {
		new DialogPractice2();

	}

}
