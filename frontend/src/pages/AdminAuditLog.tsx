const AdminAuditLog = () => {
  const events = [
    { id: 1, action: "ticket_created", actor: "Иван Житель" },
    { id: 2, action: "ticket_updated", actor: "Ольга Диспетчер" },
  ];

  return (
    <div className="grid">
      <h1>Журнал действий</h1>
      {events.map((event) => (
        <div className="card" key={event.id}>
          <p>
            <strong>{event.action}</strong> — {event.actor}
          </p>
        </div>
      ))}
    </div>
  );
};

export default AdminAuditLog;
