import { Link } from "react-router-dom";

const AdminTicketInbox = () => {
  const items = [
    { id: 41, title: "Протечка стояка", priority: "Высокий" },
    { id: 42, title: "Замена лампы", priority: "Низкий" },
  ];

  return (
    <div className="grid">
      <h1>Входящие заявки</h1>
      {items.map((item) => (
        <div className="card" key={item.id}>
          <h3>{item.title}</h3>
          <p>Приоритет: {item.priority}</p>
          <Link className="button" to={`/admin/tickets/${item.id}`}>
            Открыть
          </Link>
        </div>
      ))}
    </div>
  );
};

export default AdminTicketInbox;
