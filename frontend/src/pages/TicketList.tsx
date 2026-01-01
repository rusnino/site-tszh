import { Link } from "react-router-dom";

const TicketList = () => {
  const items = [
    { id: 1, title: "Протечка в ванной", status: "В работе" },
    { id: 2, title: "Не работает лампа в подъезде", status: "Новая" },
  ];

  return (
    <div className="grid">
      <h1>Мои заявки</h1>
      {items.map((item) => (
        <div className="card" key={item.id}>
          <h3>{item.title}</h3>
          <p>Статус: {item.status}</p>
          <Link className="button" to={`/resident/tickets/${item.id}`}>
            Открыть
          </Link>
        </div>
      ))}
    </div>
  );
};

export default TicketList;
