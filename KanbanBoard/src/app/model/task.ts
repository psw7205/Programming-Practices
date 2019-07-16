import { SubTask } from './subtask';

export class Task {
  id: number;
  title: string;
  subtasks: SubTask[];
  taskheaderID: string;
}
