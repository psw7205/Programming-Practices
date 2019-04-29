import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JTextField;

class MyDlg extends JDialog implements ActionListener {

	JTextField text;
	String str;
	JButton btn;
	JButton btn2;

	MyDlg(JFrame parent, String title, boolean modal) {
		super(parent, title, modal);
		this.setSize(300, 300);
		this.setLayout(new FlowLayout());

		text = new JTextField(20);

		btn = new JButton("OK");
		btn.addActionListener(this);
		btn2 = new JButton("CANCLE");
		btn2.addActionListener(this);


		this.add(text);
		this.add(btn);
		this.add(btn2);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if (e.getSource() == btn)
			str = text.getText();
	
		this.setVisible(false);

	}
}

public class MenuPractices extends JFrame implements ActionListener {
	JLabel label;

	MenuPractices() {
		this.setTitle("Menu");
		this.setSize(500, 500);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JMenuBar menuBar = new JMenuBar();
		JMenu menu = new JMenu("File");
		JMenu menu2 = new JMenu("File2");
		label = new JLabel();
		JMenuItem item = new JMenuItem("Open");
		menu.add(item);

		item = new JMenuItem("Save");
		menu.add(item);

		menu.addSeparator();
		item = new JMenuItem("Exit");
		menu.add(item);

		String itemStr[] = { "OPEN", "SAVE", "EXIT" };
		for (String str : itemStr) {
			JMenuItem item2 = new JMenuItem(str);
			item2.addActionListener(this);
			menu2.add(item2);
		}
		
		this.add(label);
		menuBar.add(menu);
		menuBar.add(menu2);
		this.setJMenuBar(menuBar); // 주의
		this.setVisible(true);
	}

	public static void main(String[] args) {
		new MenuPractices();
	}

	@Override
	public void actionPerformed(ActionEvent e) {

		if (e.getActionCommand().equals("OPEN")) {
			MyDlg dlg = new MyDlg(this, "OPEN DIALOG", true); // 부모, 이름, 모달(ture), 모달리스(false)
			System.out.println("Show dlg");
			dlg.setVisible(true);
			System.out.println("Close dlg");
			
			if(dlg.str != null)
				label.setText(dlg.str);
			
			System.out.println(dlg.str);
		}

		if (e.getActionCommand().equals("SAVE")) {

		}
	}

}
