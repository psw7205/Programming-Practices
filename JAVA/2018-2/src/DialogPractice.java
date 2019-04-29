import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

class StringDialog extends JDialog {
	JTextField text;
	StringDialog(JFrame frame, String title, boolean modal) {
		super(frame, title, modal);
		this.setLayout(new FlowLayout());
		
		JDialog dlg = this;
		
		text = new JTextField(20);
		text.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
		
				dlg.setVisible(false);
			}
			
		});
		add(text);

	}
}

class DialogPanel extends JPanel implements ActionListener {
	JLabel label;
	JFrame frame;
	DialogPanel() {
		label = new JLabel("label");
		JButton btn = new JButton("Push");

		btn.addActionListener(this);
		
		add(label);
		add(btn);
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		
		// 이미 완성되어 있는 다이얼로그들
		JFileChooser chooser = new JFileChooser();
		if(chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION)
		{
			label.setText(chooser.getSelectedFile().getPath());
		}
		
		
		String str = JOptionPane.showInputDialog("문자열을 입력하세요");
		if(str != null)
			label.setText(str);
		
		int result = JOptionPane.showConfirmDialog(this,  "확인하세요");
		switch(result)
		{
		case JOptionPane.YES_OPTION : 
			label.setText("예");
			break;
		case JOptionPane.NO_OPTION : 
			label.setText("아니요");
			break;
		case JOptionPane.CANCEL_OPTION : 
			label.setText("취소");
			break;
		}
		
		JOptionPane.showMessageDialog(this, "메세지출력");
		
		StringDialog dlg = new StringDialog(frame, "모달", true);
		dlg.setSize(300, 100);
		
		dlg.text.setText(label.getText());
		dlg.setVisible(true);
		
		label.setText(dlg.text.getText());

	}
}

public class DialogPractice extends JFrame {

	DialogPractice() {
		this.setSize(300, 300);
		this.setTitle("Dialog Practice");
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);

		DialogPanel p = new DialogPanel();
		p.frame = this;
		this.add(p);

		this.setVisible(true);
	}

	public static void main(String[] args) {
		new DialogPractice();

	}

}
