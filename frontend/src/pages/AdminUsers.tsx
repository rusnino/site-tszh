const AdminUsers = () => {
  const users = [
    { id: 1, name: "Иван Житель", role: "Жилец" },
    { id: 2, name: "Ольга Диспетчер", role: "Диспетчер" },
    { id: 3, name: "Павел Мастер", role: "Мастер" },
  ];

  return (
    <div className="grid">
      <h1>Пользователи</h1>
      {users.map((user) => (
        <div className="card" key={user.id}>
          <h3>{user.name}</h3>
          <p>Роль: {user.role}</p>
        </div>
      ))}
    </div>
  );
};

export default AdminUsers;
