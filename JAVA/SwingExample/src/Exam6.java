import java.awt.BorderLayout;
import java.awt.Graphics;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextArea;
import javax.swing.JTextField;

class P6 extends JPanel {

	JTextField t;
	JLabel l;
	JTextArea a;

	P6() {
		setLayout(new BorderLayout());
		
		t = new JTextField();
		l = new JLabel("asdsadasd");
		a = new JTextArea();
		
		add(t, BorderLayout.PAGE_START);
		add(a, BorderLayout.CENTER);
		add(l, BorderLayout.PAGE_END);
		
		a.setEditable(false);
		
		t.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				a.setText(a.getText() + t.getText()+"\n");
				t.setText("");
			}
			
		});
	}
	
}

public class Exam6 extends JFrame {

	Exam6() {
		setSize(500, 500);
		setDefaultCloseOperation(EXIT_ON_CLOSE);
		
		P6 p = new P6();
		add(p);
		setVisible(true);
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		new Exam6();
	}

}
