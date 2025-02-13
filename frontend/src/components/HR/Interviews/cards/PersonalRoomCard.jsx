import React from "react";
import { Card, Button, Col } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faUserTie } from "@fortawesome/free-solid-svg-icons";

const PersonalRoomCard = ({ onJoinPersonalRoom }) => {
  return (
    <Col>
      <Card className="interview-card">
        <Card.Body>
          <Card.Title>
            <FontAwesomeIcon icon={faUserTie} className="me-2" />
            Personal Room
          </Card.Title>
          <Card.Text>Join your personal meeting room.</Card.Text>
          <Button
            variant="primary"
            className="w-100"
            onClick={onJoinPersonalRoom}
          >
            Join Room
          </Button>
        </Card.Body>
      </Card>
    </Col>
  );
};

export default PersonalRoomCard;
