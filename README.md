import javax.swing.*;
import java.util.ArrayList;
import java.util.Comparator;

class Task {
    String taskName;
    int taskNumber;
    String taskDescription;
    String developer;
    int duration;
    String taskID;
    String status;

    public Task(String taskName, int taskNumber, String taskDescription, String developer, int duration, String status) {
        this.taskName = taskName;
        this.taskNumber = taskNumber;
        this.taskDescription = taskDescription;
        this.developer = developer;
        this.duration = duration;
        this.taskID = (taskName.substring(0, 2) + ":" + taskNumber + ":" +
                developer.substring(developer.length() - 3)).toUpperCase();
        this.status = status;
    }

    @Override
    public String toString() {
        return "Task Status: " + status + "\n" +
                "Developer: " + developer + "\n" +
                "Task Number: " + taskNumber + "\n" +
                "Task Name: " + taskName + "\n" +
                "Task Description: " + taskDescription + "\n" +
                "Task ID: " + taskID + "\n" +
                "Duration: " + duration + " hours\n";
    }
}

public class EasyKanban {
    static ArrayList<Task> tasks = new ArrayList<>();

    public static void main(String[] args) {
        login();
    }

    public static void login() {
        String userID = JOptionPane.showInputDialog("Enter User ID:");
        String password = JOptionPane.showInputDialog("Enter Password:");

        if (userID.equals("admin") && password.equals("1234")) {
            JOptionPane.showMessageDialog(null, "Welcome to EasyKanban");
            mainMenu();
        } else {
            JOptionPane.showMessageDialog(null, "Invalid login. Try again.");
            login();
        }
    }

    public static void mainMenu() {
        while (true) {
            String menu = """
                    Select an option:
                    1. Add tasks
                    2. Query tasks
                    3. Display all tasks
                    4. Quit
                    """;

            String choice = JOptionPane.showInputDialog(menu);

            switch (choice) {
                case "1":
                    addTasks();
                    break;
                case "2":
                    queryTasks();
                    break;
                case "3":
                    displayAllTasks();
                    break;
                case "4":
                    JOptionPane.showMessageDialog(null, "Goodbye!");
                    System.exit(0);
                    break;
                default:
                    JOptionPane.showMessageDialog(null, "Invalid choice. Try again.");
            }
        }
    }

    public static void addTasks() {
        int numberOfTasks = Integer.parseInt(JOptionPane.showInputDialog("How many tasks do you want to add?"));

        for (int i = 0; i < numberOfTasks; i++) {
            String taskName = JOptionPane.showInputDialog("Enter Task Name:");
            String taskDescription = JOptionPane.showInputDialog("Enter Task Description (max 50 characters):");
            while (taskDescription.length() > 50) {
                taskDescription = JOptionPane.showInputDialog("Description too long. Enter again (max 50 characters):");
            }

            String developer = JOptionPane.showInputDialog("Enter Developer (First and Last Name):");
            int duration = Integer.parseInt(JOptionPane.showInputDialog("Enter Task Duration (in hours):"));

            String[] statuses = {"To DO", "Done", "Doing"};
            String status = (String) JOptionPane.showInputDialog(null, "Select Task Status:",
                    "Status", JOptionPane.QUESTION_MESSAGE, null, statuses, statuses[0]);

            Task task = new Task(taskName, i, taskDescription, developer, duration, status);
            tasks.add(task);

            JOptionPane.showMessageDialog(null, "Task successfully captured:\n" + task.toString());
        }
    }

    public static void queryTasks() {
        String menu = """
                Select a query option:
                a. Display tasks with status 'done'
                b. Task with the longest duration
                c. Search by Task Name
                d. Search tasks by Developer
                e. Delete a task by Task Name
                """;

        String choice = JOptionPane.showInputDialog(menu);

        switch (choice) {
            case "a":
                displayDoneTasks();
                break;
            case "b":
                taskWithLongestDuration();
                break;
            case "c":
                searchByTaskName();
                break;
            case "d":
                searchByDeveloper();
                break;
            case "e":
                deleteTaskByName();
                break;
            default:
                JOptionPane.showMessageDialog(null, "Invalid choice. Try again.");
        }
    }

    public static void displayDoneTasks() {
        StringBuilder result = new StringBuilder("Tasks with status 'done':\n");
        for (Task task : tasks) {
            if (task.status.equalsIgnoreCase("Done")) {
                result.append("Developer: ").append(task.developer).append("\n")
                        .append("Task Name: ").append(task.taskName).append("\n")
                        .append("Task Duration: ").append(task.duration).append(" hours\n\n");
            }
        }
        JOptionPane.showMessageDialog(null, result.toString());
    }

    public static void taskWithLongestDuration() {
        Task longestTask = tasks.stream().max(Comparator.comparingInt(t -> t.duration)).orElse(null);
        if (longestTask != null) {
            JOptionPane.showMessageDialog(null, "Task with longest duration:\n" +
                    "Developer: " + longestTask.developer + "\n" +
                    "Duration: " + longestTask.duration + " hours");
        } else {
            JOptionPane.showMessageDialog(null, "No tasks available.");
        }
    }

    public static void searchByTaskName() {
        String taskName = JOptionPane.showInputDialog("Enter Task Name to search:");
        for (Task task : tasks) {
            if (task.taskName.equalsIgnoreCase(taskName)) {
                JOptionPane.showMessageDialog(null, "Task Found:\n" +
                        "Task Name: " + task.taskName + "\n" +
                        "Developer: " + task.developer + "\n" +
                        "Status: " + task.status);
                return;
            }
        }
        JOptionPane.showMessageDialog(null, "Task not found.");
    }

    public static void searchByDeveloper() {
        String developer = JOptionPane.showInputDialog("Enter Developer Name:");
        StringBuilder result = new StringBuilder("Tasks assigned to " + developer + ":\n");
        for (Task task : tasks) {
            if (task.developer.equalsIgnoreCase(developer)) {
                result.append("Task Name: ").append(task.taskName).append("\n")
                        .append("Task Status: ").append(task.status).append("\n\n");
            }
        }
        JOptionPane.showMessageDialog(null, result.toString());
    }

    public static void deleteTaskByName() {
        String taskName = JOptionPane.showInputDialog("Enter Task Name to delete:");
        tasks.removeIf(task -> task.taskName.equalsIgnoreCase(taskName));
        JOptionPane.showMessageDialog(null, "Task deleted if it existed.");
    }

    public static void displayAllTasks() {
        StringBuilder result = new StringBuilder("All Tasks:\n");
        for (Task task : tasks) {
            result.append(task.toString()).append("\n");
        }
        JOptionPane.showMessageDialog(null, result.toString());
    }
}
